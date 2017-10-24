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

def show_matches(img1, img2, coords1, coords2, matches, show=False):
    img_h = max(img1.shape[0], img2.shape[0])
    img_w = img1.shape[1] + img2.shape[1]
    out = np.zeros((img_h, img_w, 3), dtype=img1.dtype)
    out[0 : img1.shape[0], : img1.shape[1], :] = img1
    out[0 : img2.shape[0], img1.shape[1] :, :] = img2
    for m_1, m_2 in matches:
        h_1, w_1 = coords1[m_1]
        h_2, w_2 = coords2[m_2]
        w_2 += img1.shape[1]
        cv2.circle(out, (w_1, h_1), 2, (0, 255, 0), 2)
        cv2.circle(out, (w_2, h_2), 2, (0, 255, 0), 2)
        cv2.line(out, (w_1, h_1), (w_2, h_2), (255, 0, 0), 2)
    if show:
        show_bgr(out)
    else:
        return out

def show_stitch(img1, img2, show=False):
    img_h = max(img1.shape[0], img2.shape[0])
    img_w = max(img1.shape[1], img2.shape[1])
    out = np.zeros((img_h, img_w, 3), dtype=img1.dtype)
    out[0 : img1.shape[0], 0 : img1.shape[1], :] += img1 / 2
    out[0 : img2.shape[0], 0 : img2.shape[1], :] += img2 / 2
    if show:
        show_bgr(out)
    else:
        return out
