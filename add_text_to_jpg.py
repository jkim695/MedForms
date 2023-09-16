from PIL import Image, ImageDraw, ImageFont

def add_text_to_image(input_image_path, output_image_path, text, position=(10, 10), font_size=20, text_color=(255, 255, 255)):
    try:
        # Open the image
        image = Image.open(input_image_path)

        # Create a drawing object
        draw = ImageDraw.Draw(image)

        # Load a font
        font = ImageFont.load_default()

        # Set text position, font size, and color
        x, y = position
        font =  ImageFont.load_default()
        draw.text((x, y), text, font=font, fill=text_color)

        # Save the edited image
        image.save(output_image_path)

        print("Text added to image successfully.")

    except Exception as e:
        print("An error occurred:", str(e))


# Replace with the actual paths to your files and desired text
input_image_path = "1694880457959-c696be11-7d15-4f4a-a6a5-f66b1a543d4020) FINALV_1.jpg"
output_image_path = "1694880457959-c696be11-7d15-4f4a-a6a5-f66b1a543d4020) FINALV_1 copy.jpg"
text_to_add = "12345678910"
text_position = (249, 305)  # (x, y) coordinates
font_size = 20
text_color = (255, 0, 0)  # RGB color tuple (white in this case)

# Add text to the image
add_text_to_image(input_image_path, output_image_path, text_to_add, text_position, font_size, text_color)
