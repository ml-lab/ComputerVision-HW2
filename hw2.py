import numpy as np
import cv2
import matplotlib.pyplot as plt
import utils


""" find corners """
img = cv2.imread('data/bikes1.png')
cns = utils.detect_features.detect_features(img)
utils.visualize.show_corners(img, cns, show=True)

