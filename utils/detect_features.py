import cv2
import numpy as np
import matplotlib.pyplot as plt
from nonmaxsuppts import nonmaxsuppts

def conv(img, kernel):
    """ convolution kernel is assumed 3x3 """
    ret = np.zeros_like(img)
    for y in range(1, img.shape[0] - 1):
        for x in range(1, img.shape[1] - 1):
            for yy in range(3):
                for xx in range(3):
                    ret[y, x] += img[y - 1 + yy, x -1 + xx] * kernel[yy][xx]
    return ret

def gradients(img):
    """ compute graidents using Sobel operator """
    g_x = [ [ 1,  0, -1],
            [ 2,  0, -2],
            [ 1,  0, -1] ]
    g_y = [ [ 1,  2,  1],
            [ 0,  0,  0],
            [-1, -2, -1] ]
    return [conv(img, g_x), conv(img, g_y)]

def fit_elliptical_disk(g_x, g_y):
    """ Inputs: gradients Outpus: lambda_1, lambda_2 Block: 5x5 """
    l_1 = np.zeros_like(g_x)
    l_2 = np.zeros_like(g_y)
    for y in range(2, l_1.shape[0] - 2):
        for x in range(2, l_1.shape[1] - 2):
            p_x = g_x[y - 2 : y + 3, x - 2 : x + 3]
            p_y = g_y[y - 2 : y + 3, x - 2 : x + 3]
            a = np.sum(p_x * p_x)
            b = 2 * np.sum(p_x * p_y)
            c = np.sum(p_y * p_y)
            l_1[y, x] = 0.5 * (a + c + np.sqrt(b ** 2 + (a - c) ** 2))
            l_2[y, x] = 0.5 * (a + c - np.sqrt(b ** 2 + (a - c) ** 2))
    return l_1, l_2

def cornerness(l_1, l_2):
    k = 0.04
    ret = np.zeros_like(l_1)
    for y in range(l_1.shape[0]):
        for x in range(l_2.shape[1]):
            ret[y, x] = l_1[y, x] * l_2[y, x] - ((l_1[y, x] + l_2[y, x]) ** 2) * k
    return ret


def detect_features(image):
    """
    Computer Vision 600.461/661 Assignment 2
    Args:
        image (numpy.ndarray): The input image to detect features on. Note: this is NOT the image name or image path.
    Returns:
        pixel_coords (list of tuples): A list of (row,col) tuples of detected feature locations in the image
    """

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = np.float64(gray) / 255
    g_x, g_y = gradients(gray)
    l_1, l_2 = fit_elliptical_disk(g_x, g_y)
    cor = cornerness(l_1, l_2)
    pixel_coords = nonmaxsuppts(cor, 2, 0.1 * cor.max())

    return pixel_coords
