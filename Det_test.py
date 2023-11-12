from ultralytics import YOLO
import os
import cv2

model = YOLO(os.path.expanduser('~/Whitner_det/last_48_9_W.pt'))
clip_limit = 78  # Set your desired clip limit (78 in this example)
tile_size = 20


if __name__ == '__main__':
    image = cv2.imread("24.jpg", cv2.IMREAD_GRAYSCALE)

    # Create an instance of the CLAHE (Contrast Limited Adaptive Histogram Equalization) class
    clahe = cv2.createCLAHE(clipLimit=clip_limit / 10.0, tileGridSize=(tile_size, tile_size))

    # Apply AHE to the image
    equalized_image = clahe.apply(image)

    # Create an instance of the CLAHE (Contrast Limited Adaptive Histogram Equalization) class
    clahe = cv2.createCLAHE(clipLimit=clip_limit / 10.0, tileGridSize=(tile_size, tile_size))

    # Apply AHE to the image
    equalized_image = clahe.apply(image)
    bgr_image = cv2.cvtColor(equalized_image, cv2.COLOR_GRAY2BGR)
    model.predict(bgr_image, save=True, show=True)
    cv2.waitKey(0)


