from ultralytics import YOLO
import os
import cv2

model = YOLO(os.path.expanduser('~/Whitner_det/best_W_3.pt'))
clip_limit = 78  # Set your desired clip limit (78 in this example)
tile_size = 20

def predict(img):

    while True:
        image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
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
        cv2.waitKey(1)




if __name__ == '__main__':
    image = cv2.imread('your_image.jpg')

    predict(image)

