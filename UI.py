from ultralytics import YOLO
import os
import cv2
import time
model = YOLO(os.path.expanduser('~/Whitner_det/best_W_3.pt'))
clip_limit = 78  # Set your desired clip limit (78 in this example)
tile_size = 20

def predict(img):
    image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Create an instance of the CLAHE (Contrast Limited Adaptive Histogram Equalization) class
    clahe = cv2.createCLAHE(clipLimit=clip_limit / 10.0, tileGridSize=(tile_size, tile_size))
    width, height, channels = img.shape

    print('Image width:', width)
    print('Image height:', height)
    # Apply AHE to the image
    equalized_image = clahe.apply(image)

    # Create an instance of the CLAHE (Contrast Limited Adaptive Histogram Equalization) class
    clahe = cv2.createCLAHE(clipLimit=clip_limit / 10.0, tileGridSize=(tile_size, tile_size))

    # Apply AHE to the image
    equalized_image = clahe.apply(image)
    bgr_image = cv2.cvtColor(equalized_image, cv2.COLOR_GRAY2BGR)
    #img = cv2.resize(img, (2048, 1152))
    #bgr_image = cv2.resize(bgr_image, (2048, 2048))
    #model.predict(bgr_image, save=True, show=True,imgsz=(2048,2048))
    results = model(bgr_image,imgsz=(2048,2048))
    #results = model(resized_image)
    for result in results:
        boxes = result.boxes  # Boxes object for bbox outputs
        masks = result.masks  # Masks object for segmentation masks outputs
        keypoints = result.keypoints  # Keypoints object for pose outputs
        probs = result.probs  # Probs object for classification outputs

        for box in boxes:
            # print(box.xywh)
            if (int(box.cls) == 0):
                x = int(box.xywh[0][0])
                y = int(box.xywh[0][1])
                w = int(box.xywh[0][2])
                h = int(box.xywh[0][3])
                i = int(box.cls)
                cv2.rectangle(img, (x-int(w/2), y-int(h/2)), ((x + int(w/2)), (y + int(h/2))), (0, 0, 255), thickness=4)


    return img

if __name__ == '__main__':
    image = cv2.imread('13.jpg')

    final=predict(image)
    resized_image = cv2.resize(image, (900,900))
    cv2.imshow("out", resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    time.sleep(10)
