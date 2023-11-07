import cv2
import numpy as np
import tkinter as tk
from tkinter import Scale

# Function to update the HSV values and display the image
def update_hsv_image(h, s, v):
    updated_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV).astype(np.int16)
    updated_image[:, :, 0] = (updated_image[:, :, 0] + h) % 180  # Ensure Hue wraps around [0, 179]
    updated_image[:, :, 1] = np.clip(updated_image[:, :, 1] + s, 0, 255)  # Clip Saturation to [0, 255]
    updated_image[:, :, 2] = np.clip(updated_image[:, :, 2] + v, 0, 255)  # Clip Value to [0, 255]
    updated_image = cv2.cvtColor(updated_image.astype(np.uint8), cv2.COLOR_HSV2BGR)
    updated_image = cv2.resize(updated_image, (900, 900))
    cv2.imshow("Updated Image", updated_image)

# Load the original image
original_image = cv2.imread('17.jpg')

# Create a GUI window
root = tk.Tk()
root.title("HSV Adjustment")

# Create sliders for Hue, Saturation, and Value
h_slider = Scale(root, label="Hue (-180 to 180)", from_=-180, to=180, orient="horizontal", length=300, resolution=1)
s_slider = Scale(root, label="Saturation (-255 to 255)", from_=-255, to=255, orient="horizontal", length=300, resolution=1)
v_slider = Scale(root, label="Value (-255 to 255)", from_=-255, to=255, orient="horizontal", length=300, resolution=1)

# Set initial slider values
h_slider.set(0)
s_slider.set(0)
v_slider.set(0)

# Pack the GUI elements
h_slider.pack()
s_slider.pack()
v_slider.pack()

# Start the main loop
root.update()  # Initialize the GUI elements

while True:
    root.update()  # Update the GUI elements

    h = h_slider.get()
    s = s_slider.get()
    v = v_slider.get()

    update_hsv_image(h, s, v)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

# Release OpenCV windows and close the program
cv2.destroyAllWindows()