import cv2

# Load the image in grayscale
image = cv2.imread('Sample1.jpg', cv2.IMREAD_GRAYSCALE)

# Define the parameters for Adaptive Histogram Equalization (AHE)
clip_limit = 2.0  # Adjust this value as needed
tile_size = (8, 8)  # Adjust the tile size as needed

# Create an instance of the CLAHE (Contrast Limited Adaptive Histogram Equalization) class
clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_size)

# Apply AHE to the image
equalized_image = clahe.apply(image)

# Display the original and equalized images
cv2.imshow('Original Image', image)
cv2.imshow('Equalized Image', equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()