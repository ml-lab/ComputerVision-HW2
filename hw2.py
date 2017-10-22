import numpy as np
import cv2
import matplotlib.pyplot as plt
import utils
import os

comp_list = [
    ['bikes1', 'bikes2'],
    ['bikes1', 'bikes3'],
    ['graf1', 'graf2'],
    ['graf1', 'graf3'],
    ['leuven1', 'leuven2'],
    ['leuven1', 'leuven3'],
    ['wall1', 'wall2'],
    ['wall1', 'wall3']
]

for img_path_1, img_path_2 in comp_list:
    img1 = cv2.imread(os.path.join('data', img_path_1 + '.png'))
    cns1 = utils.detect_features.detect_features(img1)
    save = utils.visualize.show_corners(img1, cns1, show=False)
    cv2.imwrite(os.path.join('results', img_path_1 + '_corners.png'), save)

    img2 = cv2.imread(os.path.join('data', img_path_2 + '.png'))
    cns2 = utils.detect_features.detect_features(img2)
    save = utils.visualize.show_corners(img2, cns2, show=False)
    cv2.imwrite(os.path.join('results', img_path_2 + '_corners.png'), save)

    matches = utils.match_features.match_features(cns1, cns2, img1, img2)
    save = utils.visualize.show_matches(img1, img2, cns1, cns2, matches, show=False)
    cv2.imwrite(os.path.join('results', img_path_1 + '_' + img_path_2 + '_matches.png'), save)

    matrix = utils.compute_affine_xform.compute_affine_xform(matches, cns1, cns2, img1, img2)
    if matrix is None:
        img2_warped = np.zeros_like(img1)
    else:
        img2_warped = cv2.warpAffine(img1, matrix[0:2, 0:3], (img1.shape[1], img1.shape[0]))
    cv2.imwrite(os.path.join('results', img_path_2 + '_affine_warped_from_' + img_path_1 + '.png'), img2_warped)

    matrix = utils.compute_proj_xform.compute_proj_xform(matches, cns1, cns2, img1, img2)
    if matrix is None:
        img2_warped = np.zeros_like(img1)
    else:
        img2_warped = cv2.warpPerspective(img1, matrix[0:3, 0:3], (img1.shape[1], img1.shape[0]))
    cv2.imwrite(os.path.join('results', img_path_2 + '_perspective_warped_from_' + img_path_1 + '.png'), img2_warped)

    matches = utils.ssift_descriptor.match_features(cns1, cns2, img1, img2)
    save = utils.visualize.show_matches(img1, img2, cns1, cns2, matches, show=False)
    cv2.imwrite(os.path.join('results', img_path_1 + '_' + img_path_2 + '_ssift_matches.png'), save)

    matrix = utils.compute_affine_xform.compute_affine_xform(matches, cns1, cns2, img1, img2)
    if matrix is None:
        img2_warped = np.zeros_like(img1)
    else:
        img2_warped = cv2.warpAffine(img1, matrix[0:2, 0:3], (img1.shape[1], img1.shape[0]))
    cv2.imwrite(os.path.join('results', img_path_2 + '_ssift_affine_warped_from_' + img_path_1 + '.png'), img2_warped)

    matrix = utils.compute_proj_xform.compute_proj_xform(matches, cns1, cns2, img1, img2)
    if matrix is None:
        img2_warped = np.zeros_like(img1)
    else:
        img2_warped = cv2.warpPerspective(img1, matrix[0:3, 0:3], (img1.shape[1], img1.shape[0]))
    cv2.imwrite(os.path.join('results', img_path_2 + '_ssift_perspective_warped_from_' + img_path_1 + '.png'), img2_warped)

