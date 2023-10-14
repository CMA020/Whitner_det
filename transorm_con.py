import cv2
import os

def equalize_and_save_image(input_folder, output_folder, clip_limit=20, tile_size=8):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg"):  # Change the file extension as needed
            image_path = os.path.join(input_folder, filename)

            # Load the image in grayscale
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            # Create an instance of the CLAHE (Contrast Limited Adaptive Histogram Equalization) class
            clahe = cv2.createCLAHE(clipLimit=clip_limit / 10.0, tileGridSize=(tile_size, tile_size))

            # Apply AHE to the image
            equalized_image = clahe.apply(image)

            # Save the equalized image to the output folder
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, equalized_image)

if __name__ == "__main__":
    input_folder = os.path.expanduser("~/Downloads/Whitner")  # Replace with the path to your input folder
    output_folder = os.path.expanduser("~/Downloads/White2") # Replace with the path to your output folder

    clip_limit = 78  # Set your desired clip limit (78 in this example)
    tile_size = 20  # Set your desired tile size (32 in this example)

    equalize_and_save_image(input_folder, output_folder, clip_limit, tile_size)