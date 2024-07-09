from PIL import Image

# Replace 'your_image.jpg' with the path to your image file
image_path = './your_image.jpg'
image = Image.open(image_path)

# Convert the image to RGB (just in case it's in a different format)
image_rgb = image.convert('RGB')

# Specify the coordinates of the pixel you want to inspect
x = 100  # X coordinate
y = 50   # Y coordinate

# Get the RGB values of the pixel at the specified coordinates
rgb_value = image_rgb.getpixel((x, y))

print(f"The RGB value of the pixel at position ({x}, {y}) is {rgb_value}")
