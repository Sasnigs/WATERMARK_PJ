from PIL import Image, ImageDraw, ImageFont
import os

def add_watermark_to_folder(input_folder, output_folder, watermark_text, font_path, font_size=150, transparency= 70):
    try:
        # Validate input and output folders
        if not os.path.exists(input_folder):
            raise FileNotFoundError(f"Input folder '{input_folder}' not found.")
        
        # Create output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True) 

        # Validate font file
        if not os.path.exists(font_path):
            raise FileNotFoundError(f"Font file '{font_path}' not found.")

        # List all files in the input folder
        files = os.listdir(input_folder)

        # Filter image files
        image_files = [file for file in files if file.lower().endswith(('jpg', 'jpeg', 'png', 'bmp', 'gif'))]

        if not image_files:
            print(f"No image files found in {input_folder}.")
            return

        # Process each image file
        for image_file in image_files:
            try:
                # Open the image
                image_path = os.path.join(input_folder, image_file)
                image = Image.open(image_path).convert('RGBA')

                # Define the font
                font = ImageFont.truetype(font_path, font_size)

                # Calculate position for the watermark (center of the image)
                text_bbox = font.getbbox(watermark_text)
                text_width = text_bbox[2] - text_bbox[0]
                text_height = text_bbox[3] - text_bbox[1]
                x = (image.width - text_width) / 2
                y = (image.height - text_height) / 2

                # Create a transparent overlay
                watermark = Image.new('RGBA', image.size, (0, 0, 0, 0))

                # Draw the watermark text
                draw = ImageDraw.Draw(watermark)
                draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, transparency))  # fill = White text with transparency

                # Combine the original image with the watermark
                watermarked_image = Image.alpha_composite(image, watermark)
                
                # Convert back to RGB mode for JPEG images
                if image_file.lower().endswith(('jpg', 'jpeg')):
                    watermarked_image = watermarked_image.convert('RGB')

                # Save the watermarked image
                output_path = os.path.join(output_folder, f"watermarked_{image_file}")
                watermarked_image.save(output_path)

                print(f"Watermarked image saved as: {output_path}")

            except Exception as e:
                print(f"Error processing {image_file}: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")
def main():
    input_folder = input("File path of images to be watermarked: ")
    output_folder = input("File path for saved watermark images: ")
    watermark_text = input("Watermark Text: ")
    font_path = "fonts/Arial Unicode.ttf"
    font_size = int(input("Interger Font_size: "))
    transparency = int(input("Text transparency( 0 - 255 where 0 is fully transparent and 255 is fully opaque): "))

    add_watermark_to_folder(input_folder, output_folder, watermark_text, font_path, font_size, transparency)

if __name__== "__main__":
    main()