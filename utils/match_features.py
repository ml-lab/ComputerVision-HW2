import numpy as np
import cv2
import matplotlib.pyplot as plt

def get_patches(img, coords, k=20):
    ret = []
    pad = np.zeros((img.shape[0] + 2 * k, img.shape[1] + 2 * k, 3), dtype=img.dtype)
    pad[k : -k, k : -k, :] = img
    for y, x in coords:
        ret.append(pad[y : y + 2 * k + 1, x : x + 2 * k + 1, :])
    return ret

def ssd_dist(pat_1, pat_2):
    return np.sum((pat_1 - pat_2) ** 2)

def get_best(pat_test, pat_2_ref):
    ret = []
    for pat_1 in pat_test:
        min_dst = 1e16
        min_idx = 0
        for idx in range(len(pat_2_ref)):
            dist = ssd_dist(pat_1, pat_2_ref[idx])
            if dist < min_dst:
                min_dst = dist
                min_idx = idx
        ret.append(min_idx)
    return ret

def marriage(bst_1, bst_2):
    ret = []
    for idx in range(len(bst_1)):
        ref_1 = bst_1[idx]
        if bst_2[ref_1] == idx:
            ret.append([idx, ref_1])
    return ret

def match_features(feature_coords1,feature_coords2,image1,image2):
    """
    Computer Vision 600.461/661 Assignment 2
    Args:
        feature_coords1 (list of tuples): list of (row,col) tuple feature coordinates from image1
        feature_coords2 (list of tuples): list of (row,col) tuple feature coordinates from image2
        image1 (numpy.ndarray): The input image corresponding to features_coords1
        image2 (numpy.ndarray): The input image corresponding to features_coords2
    Returns:
        matches (list of tuples): list of index pairs of possible matches. For example, if the 4-th feature in feature_coords1 and the 0-th feature
                                  in feature_coords2 are determined to be matches, the list should contain (4,0).
    """

    pat_1 = get_patches(image1, feature_coords1)
    pat_2 = get_patches(image2, feature_coords2)
    bst_1 = get_best(pat_1, pat_2)
    bst_2 = get_best(pat_2, pat_1)
    matches = marriage(bst_1, bst_2)
    return matches
