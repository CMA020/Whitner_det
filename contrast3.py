import cv2
import numpy as np


def update_clahe(_):
    clip_limit = cv2.getTrackbarPos('Clip Limit', 'Equalized Image')
    tile_size = cv2.getTrackbarPos('Tile Size', 'Equalized Image')

    # Create an instance of the CLAHE (Contrast Limited Adaptive Histogram Equalization) class
    clahe = cv2.createCLAHE(clipLimit=clip_limit / 10.0, tileGridSize=(tile_size, tile_size))

    # Resize the image to a fixed size while maintaining its aspect ratio
    aspect_ratio = image.shape[1] / image.shape[0]  # Width / Height
    new_width = 900
    new_height = int(new_width / aspect_ratio)
    resized_image = cv2.resize(image, (new_width, new_height))

    # Apply AHE to the resized image
    equalized_image = clahe.apply(resized_image)

    # Display the equalized image in the fixed-size window
    cv2.imshow('Equalized Image', equalized_image)


# Load the image in grayscale
image = cv2.imread('8.jpg', cv2.IMREAD_GRAYSCALE)

# Create a window for the equalized image with a fixed size
cv2.namedWindow('Equalized Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Equalized Image', 900, 800)

# Create trackbars for clip limit and tile size
cv2.createTrackbar('Clip Limit', 'Equalized Image', 20, 100, update_clahe)
cv2.createTrackbar('Tile Size', 'Equalized Image', 8, 32, update_clahe)

# Initialize the equalized image with default parameters
update_clahe(0)

# Loop to keep the window open
while True:
    key = cv2.waitKey(1)
    if key == 27:  # Press 'Esc' to exit
        break

cv2.destroyAllWindows()