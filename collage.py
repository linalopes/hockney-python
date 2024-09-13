import cv2
import numpy as np
import glob
import random

# Function to add a white border to the image
def add_border(image, border_size=2):
    return cv2.copyMakeBorder(image, border_size, border_size, border_size, border_size, cv2.BORDER_CONSTANT, value=[255, 255, 255])

# Load images
image_files = [f'_MG_{i}.JPG' for i in range(9789, 9828)]
images = [cv2.imread(img) for img in image_files]

# Resize images for better visualization
resized_images = [cv2.resize(img, (600, 400)) for img in images]

# Add border to each image
bordered_images = [add_border(img) for img in resized_images]

# Initialize the collage canvas
collage_height = 3000
collage_width = 5000
collage = np.ones((collage_height, collage_width, 3), dtype=np.uint8) * 255

# Initialize SIFT detector
sift = cv2.SIFT_create()

# Detect keypoints and descriptors
keypoints_descriptors = [sift.detectAndCompute(img, None) for img in bordered_images]

# Initialize FLANN matcher
index_params = dict(algorithm=1, trees=5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params, search_params)

# Start with the first image in the center
base_img = bordered_images[0]
h, w = base_img.shape[:2]
collage_center_x = collage_width // 2 - w // 2
collage_center_y = collage_height // 2 - h // 2
collage[collage_center_y:collage_center_y+h, collage_center_x:collage_center_x+w] = base_img
placed_images = [(collage_center_y, collage_center_x, h, w, base_img, keypoints_descriptors[0])]

# Function to find the best match position for the next image
def find_best_match_position(img, kp_des, placed_images):
    best_match = None
    best_position = None
    for (y, x, h, w, placed_img, kp_des_placed) in placed_images:
        matches = flann.knnMatch(kp_des[1], kp_des_placed[1], k=2)
        good_matches = [m for m, n in matches if m.distance < 0.7 * n.distance]
        if len(good_matches) > 10:
            src_pts = np.float32([kp_des[0][m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
            dst_pts = np.float32([kp_des_placed[0][m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)
            M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
            if M is not None:
                h, w = img.shape[:2]
                pts = np.float32([[0, 0], [0, h], [w, h], [w, 0]]).reshape(-1, 1, 2)
                dst = cv2.perspectiveTransform(pts, M)
                dst += np.float32([[[x, y]]])
                min_x, min_y = np.int32(dst.min(axis=0).ravel() - 0.5)
                max_x, max_y = np.int32(dst.max(axis=0).ravel() + 0.5)
                if min_x >= 0 and min_y >= 0 and max_x <= collage_width and max_y <= collage_height:
                    if best_match is None or len(good_matches) > best_match:
                        best_match = len(good_matches)
                        best_position = (min_y, min_x)
    return best_position

# Place the rest of the images based on the best match position
for i in range(1, len(bordered_images)):
    best_position = find_best_match_position(bordered_images[i], keypoints_descriptors[i], placed_images)
    if best_position:
        y, x = best_position
        h, w = bordered_images[i].shape[:2]
        
        # Random rotation
        angle = random.uniform(-5, 5)
        M = cv2.getRotationMatrix2D((w // 2, h // 2), angle, 1)
        rotated_img = cv2.warpAffine(bordered_images[i], M, (w, h), borderValue=(255, 255, 255))
        
        # Ensure the images are within canvas boundaries
        if x + w <= collage_width and y + h <= collage_height:
            blend_region = collage[y:y+h, x:x+w]
            mask = (rotated_img > 0).astype(np.uint8) * 255
            blended = cv2.seamlessClone(rotated_img, blend_region, mask, (w // 2, h // 2), cv2.MIXED_CLONE)
            collage[y:y+h, x:x+w] = blended
        
            placed_images.append((y, x, h, w, bordered_images[i], keypoints_descriptors[i]))

# Save the final collage
cv2.imwrite('hockney_collage.jpg', collage)
print("Collage created successfully. Saved as 'hockney_collage.jpg'.")

# Optionally display the collage
cv2.imshow('Hockney Collage', collage)
cv2.waitKey(0)
cv2.destroyAllWindows()
