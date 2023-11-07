import cv2
import numpy as np

# Function to update the eroded image based on the kernel size
def update_image(erode_size):
    kernel = np.ones((erode_size, erode_size), np.uint8)
    eroded_image = cv2.erode(original_image, kernel, iterations=1)
    cv2.imshow('Eroded Image', eroded_image)

# Load the image
original_image = cv2.imread('your_image.jpg')

# Create a window to display the image
cv2.namedWindow('Eroded Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Eroded Image', 900, 900)

# Initial kernel size
kernel_size = 5

# Create a trackbar/slider to change the kernel size
cv2.createTrackbar('Kernel Size', 'Eroded Image', kernel_size, 20, update_image)

while True:
    key = cv2.waitKey(1) & 0xFF

    # Exit the loop if the 'q' key is pressed
    if key == ord('q'):
        break

cv2.destroyAllWindows()