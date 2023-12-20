from PIL import Image

def split_image(image_path):
    # Open the image
    img = Image.open(image_path)

    # Get the size of the image
    width, height = img.size

    # Calculate the dimensions for each of the 9 parts
    part_width = width // 3
    part_height = height // 3

    parts = []

    # Iterate through each row and column to extract parts
    for i in range(3):
        for j in range(3):
            left = j * part_width
            upper = i * part_height
            right = (j + 1) * part_width
            lower = (i + 1) * part_height

            # Crop the image to extract the current part
            part = img.crop((left, upper, right, lower))
            parts.append(part)

    return parts

# Example usage
image_path = "t3.jpeg"
image_parts = split_image(image_path)

# Save or display the individual parts as needed
for idx, part in enumerate(image_parts):
    part.save(f"part_{idx + 1}.jpg")  # Save each part as a separate image