import numpy as np
import cv2
import matplotlib.pyplot as plt

def show_bgr(img):
    b, g, r = cv2.split(img)
    rgb_img = cv2.merge([r, g, b])
    plt.imshow(rgb_img)
    plt.show()

def show_corners(img, corners, show=False):
    out = img.copy()
    for row, col in corners:
        cv2.circle(out, (col, row), 2, (0, 255, 0), 2)
    if show:
        show_bgr(out)
    else:
        return out
