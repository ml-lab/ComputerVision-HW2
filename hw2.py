import numpy as np
import cv2
import matplotlib.pyplot as plt
import utils

'''

""" find corners """
img = cv2.imread('data/graf1.png')
cns = utils.detect_features.detect_features(img)
# utils.visualize.show_corners(img, cns, show=True)

""" match corners """
img2 = cv2.imread('data/graf2.png')
cns2 = utils.detect_features.detect_features(img2)
matches = utils.match_features.match_features(cns, cns2, img, img2)
# utils.visualize.show_matches(img, img2, cns, cns2, matches, show=True)


np.save('tmp/cns', cns)
np.save('tmp/cns2', cns2)
np.save('tmp/matches', matches)
exit(0)


'''

img = cv2.imread('data/graf1.png')
img2 = cv2.imread('data/graf2.png')

cns = np.load('tmp/cns.npy')
cns2 = np.load('tmp/cns2.npy')
matches = np.load('tmp/matches.npy')

# utils.visualize.show_matches(img, img2, cns, cns2, matches, show=True)

""" affine """
matrix = utils.compute_proj_xform.compute_proj_xform(matches,
        cns, cns2, img, img2)
utils.compute_proj_xform.visualize_ransac(matrix, matches, cns, cns2, img, img2, show=True)
print matrix
