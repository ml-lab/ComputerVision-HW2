import numpy as np
import cv2
import matplotlib.pyplot as plt
from detect_features import gradients

def get_patches(img, coords):
    k = 20
    ret = []
    pad = np.zeros((img.shape[0] + 2 * k, img.shape[1] + 2 * k), dtype=img.dtype)
    pad[k : -k, k : -k] = img
    for y, x in coords:
        ret.append(pad[y : y + 2 * k + 1, x : x + 2 * k + 1])
    return ret

def grid_ssift(grad_y, grad_x, grad):
    ft = [0.0] * 8
    for y in range(10):
        for x in range(10):
            g_y = grad_y[y, x]
            g_x = grad_x[y, x]
            g = grad[y, x]
            if g_y > 0 and g_x > 0:
                if g_y > g_x:
                    ft[0] += g
                else:
                    ft[1] += g
            elif g_y <= 0 and g_x > 0:
                if -g_y > g_x:
                    ft[2] += g
                else:
                    ft[3] += g
            elif g_y > 0 and g_x <= 0:
                if g_y > -g_x:
                    ft[4] += g
                else:
                    ft[5] += g
            else:
                if g_y > g_x:
                    ft[6] += g
                else:
                    ft[7] += g
    return ft

def normalize(array):
    array = array / np.sqrt(np.sum(array ** 2))
    array[array > 0.2] = 0.2
    return array / np.sqrt(np.sum(array ** 2))

def local_ssift(grad_y, grad_x, grad):
    ft = []
    for y in range(4):
        for x in range(4):
            ft += grid_ssift(grad_y[y * 10 : y * 10 + 10, x * 10 : x * 10 + 10],
                             grad_x[y * 10 : y * 10 + 10, x * 10 : x * 10 + 10],
                             grad[y * 10 : y * 10 + 10, x * 10 : x * 10 + 10])
    return normalize(np.array(ft))

def ssift(feature_coords, image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = np.float64(gray) / 255
    grad_x, grad_y = gradients(gray)
    grad = np.sqrt(grad_y ** 2 + grad_x ** 2)
    pat_x = get_patches(grad_x, feature_coords)
    pat_y = get_patches(grad_y, feature_coords)
    pat_g = get_patches(grad, feature_coords)
    descriptors = {}
    for i in range(len(feature_coords)):
        coord = feature_coords[i]
        descriptors[coord] = local_ssift(pat_y[i], pat_x[i], pat_g[i])
    return descriptors

def ssift_descriptor(feature_coords,image):
    """
    Computer Vision 600.461/661 Assignment 2
    Args:
        feature_coords (list of tuples): list of (row,col) tuple feature coordinates from image
        image (numpy.ndarray): The input image to compute ssift descriptors on. Note: this is NOT the image name or image path.
    Returns:
        descriptors (dictionary{(row,col): 128 dimensional list}): the keys are the feature coordinates (row,col) tuple and
                                                                   the values are the 128 dimensional ssift feature descriptors.
    """

    descriptors = ssift(feature_coords, image)

    return descriptors

def match_features(feature_coords1, feature_coords2, image1, image2):
    features1 = ssift(feature_coords1, image1)
    features2 = ssift(feature_coords2, image2)
    ret = []
    for i in range(len(feature_coords1)):
        coord1 = feature_coords1[i]
        ft1 = features1[coord1]
        max_sim, sim_2nd, max_idx = -1., -1., 0
        for j in range(len(feature_coords2)):
            coord2 = feature_coords2[j]
            ft2 = features2[coord2]
            sim = np.sum(ft1 * ft2)
            if sim > max_sim:
                sim_2nd = max_sim
                max_sim = sim
                max_idx = j
        if sim_2nd / max_sim < 0.75:
            ret.append([i, max_idx])
    return ret
