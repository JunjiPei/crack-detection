from PIL import Image, ImageEnhance, ImageOps


def enhance_cracks(image_path, output_path):
    # Load the image
    img = Image.open(image_path)

    # Convert the image to grayscale and invert it
    grayscale = ImageOps.grayscale(img)
    inverted_img = ImageOps.invert(grayscale)

    # Enhance the contrast of the inverted grayscale image
    enhancer = ImageEnhance.Contrast(inverted_img)
    enhanced_img = enhancer.enhance(3.0)  # Adjust the factor as needed

    # Convert back to color
    final_img = ImageOps.colorize(enhanced_img, black="black", white="white")

    # Overlay the enhanced cracks on the original image
    combined = Image.blend(img, final_img.convert('RGB'), alpha=0.3)  # Adjust alpha as needed

    # Show the final image
    combined.show()

    # Save the final image
    combined.save(output_path)


# Usage
image_path = 'cropped_image.jpg'
output_path = 'enhanced_crack_image.jpg'

enhance_cracks(image_path, output_path)
