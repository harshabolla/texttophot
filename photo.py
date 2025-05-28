from PIL import Image, ImageDraw, ImageFont

def text_to_image(text, filename="output.png"):
    # Create a blank image
    img = Image.new('RGB', (400, 100), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    # Use a default font
    font = ImageFont.load_default()
    # Add text to image
    d.text((10, 40), text, fill=(0, 0, 0), font=font)
    img.save(filename)
    print(f"Image saved as {filename}")

if __name__ == "__main__":
    user_text = input("Enter text: ")
    text_to_image(user_text)