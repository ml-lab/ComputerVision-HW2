import numpy as np
import cv2
import matplotlib.pyplot as plt
import utils


""" find corners """
img = cv2.imread('data/graf1.png')
cns = utils.detect_features.detect_features(img)
utils.visualize.show_corners(img, cns, show=True)

""" match corners """
img2 = cv2.imread('data/graf2.png')
cns2 = utils.detect_features.detect_features(img2)
matches = utils.match_features.match_features(cns, cns2, img, img2)
utils.visualize.show_matches(img, img2, cns, cns2, matches, show=True)
