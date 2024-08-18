# Image Watermarking Script

This script adds a watermark to all image files within a specified input folder and saves the watermarked images to an output folder. The watermark text, font, and font size can be customized.

## Features

- Adds a watermark text to the center of each image in the specified input folder.
- Supports various image formats, including JPG, JPEG, PNG, BMP, and GIF.
- Saves the watermarked images to the specified output folder.
- Allows customization of watermark text, font, and font size.

## Requirements
- Pillow library

## Installation
1. Install the Pillow library using pip:
    ```bash
    pip install Pillow
    ```
## Usage

1. Save the script to a file, for example `watermark.py`.
2. Run the script using Python:

    ```bash
    python3 watermark.py
    ```

3. Follow the prompts to enter:
   - The file path of the input folder containing the images.
   - The file path of the output folder where watermarked images will be saved.
   - The watermark text.
   - The file path of the font (e.g., TTF file).
   - The font size (integer).
   - The transparency of the text.

     
Video walkthrough: https://youtu.be/wyk-wb8iAfw
