# hockeney-python

https://blog.lilothink.science/using-a-15-year-old-digital-camera-to-craft-80s-style-collages-with-modern-computer-vision-code/

## Setup
### Requirements
- Python 3.7+
- OpenCV
- NumPy
- PIL (Python Imaging Library)
Install the necessary libraries using:

```bash
pip install -r requirements.txt
```

### Hardware
While this project is designed to work best with images taken on a 15-year-old digital camera, you can also use any photos from your collection for collage-making.

### Image Input
To get started, either upload your own photos or use the sample images in the data/ folder. Place your images in the input_images/ folder.

## Usage
1. Prepare Your Images: Use your digital camera or select images from your collection and place them in the input_images/ folder.
2. Run the Collage Script: Generate your collage with the following command:

```bash
python create_collage.py --input_folder input_images/ --output_folder output_collages/
````

3. Customization: Modify the collage style and layout with command-line options:
--layout: Choose from different layout styles like grid, random, or overlap.
--filter: Apply retro color filters like sepia, vintage, or high-contrast.
--size: Adjust the size of the collage output.
4. Collage Output: Your finished collage will be saved in the output_collages/ folder.