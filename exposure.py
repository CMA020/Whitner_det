import cv2

def update_exposure(_):
    brightness = cv2.getTrackbarPos('Brightness', 'Exposure Adjustment')
    contrast = cv2.getTrackbarPos('Contrast', 'Exposure Adjustment')

    # Calculate contrast and brightness values for adjusting exposure
    alpha = 1.0 + (contrast - 100) / 100.0
    beta = brightness - 50

    # Apply contrast and brightness adjustment to the image
    adjusted_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

    cv2.imshow('Exposure Adjustment', adjusted_image)

# Load the image
image = cv2.imread('4.jpg')

# Create a window for exposure adjustment
cv2.namedWindow('Exposure Adjustment', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Exposure Adjustment', 900, 800)

# Create trackbars for brightness and contrast
cv2.createTrackbar('Brightness', 'Exposure Adjustment', 50, 100, update_exposure)
cv2.createTrackbar('Contrast', 'Exposure Adjustment', 100, 200, update_exposure)

# Initialize the exposure adjustment with default parameters
update_exposure(0)

# Loop to keep the window open
while True:
    key = cv2.waitKey(1)
    if key == 27:  # Press 'Esc' to exit
        break

cv2.destroyAllWindows()