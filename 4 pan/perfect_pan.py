import cv2
import numpy as np
import glob

# Load images
image_files = glob.glob('_MG_9829.JPG') + [f'_MG_{i}.JPG' for i in range(9829, 9848)]
images = [cv2.imread(img) for img in image_files]

# Create the stitcher object
stitcher = cv2.Stitcher_create()

# Stitch images together
(status, stitched) = stitcher.stitch(images)

# Check if the stitching was successful
if status == cv2.Stitcher_OK:
    # Save the stitched image
    cv2.imwrite('stitched_output.jpg', stitched)
    print("Stitching completed successfully. Saved as 'stitched_output.jpg'.")
else:
    print(f"Error during stitching: {status}")

# Optionally display the stitched image
cv2.imshow('Stitched Image', stitched)
cv2.waitKey(0)
cv2.destroyAllWindows()
