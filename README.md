# hockeney-python

https://blog.lilothink.science/using-a-15-year-old-digital-camera-to-craft-80s-style-collages-with-modern-computer-vision-code/

## Introduction
This project brings together early 2000s digital photography with a collage-making process inspired by the bold and colorful styles of the 1980s. Using a 15-year-old digital camera, we capture raw, nostalgic images and transform them into unique 80s-style collages through modern digital editing techniques using python.

![Collage Example](2nd%20Try/2%205%20hockney_collage.jpg)

## Features
- Authentic 80s Aesthetic: Collages created with vibrant colors, geometric patterns, and retro elements that pay homage to 1980s design.
- Vintage Photography: Images are captured with a 15-year-old digital camera for an authentic low-resolution, grainy look reminiscent of early digital photography.
- Customizable Collage Layouts: Arrange and layer images with adjustable parameters for layout, color palettes, and texture effects.
- Easy Workflow: A streamlined process to turn your photos into personalized 80s-style collages with minimal effort.

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

## Inspiration
This project is inspired by the DIY spirit of the 1980s and the early days of digital photography. By using an old digital camera, we recreate the feeling of raw, unpolished photos and mix them with the playful design elements of vintage collages.

## Contributing
Feel free to contribute to this project by submitting a pull request or opening an issue. Suggestions for new collage styles or layout ideas are always welcome!

## License
This project is licensed under the MIT License. See the LICENSE file for more details.