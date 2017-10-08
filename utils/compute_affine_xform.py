# Author: TK
import numpy as np
import cv2
import matplotlib.pyplot as plt
import sympy as sp
import visualize

def get_affine_trans(src, dst):
    """ src and dst: lists of three points (y, x) """
    a = sp.Symbol('a')
    b = sp.Symbol('b')
    c = sp.Symbol('c')
    d = sp.Symbol('d')
    e = sp.Symbol('e')
    f = sp.Symbol('f')
    eq_list = []
    sm_list = [a, b, c, d, e, f]
    for i in range(3):
        eq_list.append(sp.Eq(a * src[i][1] + b * src[i][0] + c, dst[i][1]))
        eq_list.append(sp.Eq(d * src[i][1] + e * src[i][0] + f, dst[i][0]))
    solution = sp.solve(eq_list, sm_list)
    try:
        affine_xform = np.zeros((3, 3))
        affine_xform[2][2] = 1
        affine_xform[0][0] = solution[a]
        affine_xform[0][1] = solution[b]
        affine_xform[0][2] = solution[c]
        affine_xform[1][0] = solution[d]
        affine_xform[1][1] = solution[e]
        affine_xform[1][2] = solution[f]
        return affine_xform
    except:
        return None

def forward(src, mat):
    x = mat[0][0] * src[1] + mat[0][1] * src[0] + mat[0][2]
    y = mat[1][0] * src[1] + mat[1][1] * src[0] + mat[1][2]
    return [y, x]

def evaluate(matches, features1, features2, matrix, thres=10):
    acc, tlt = 0, 0
    for mat_1, mat_2 in matches:
        p_1 = features1[mat_1]
        p_2 = features2[mat_2]
        e_2 = forward(p_1, matrix)
        if abs(p_2[0] - e_2[0]) <= thres and abs(p_2[1] - e_2[1]) <= thres:
            acc += 1
        tlt += 1
    return float(acc) / tlt

def ransac(matches, features1, features2, ran_round=1000):
    max_rat, max_mat = 0.0, None
    for ran_idx in range(ran_round):
        mat_1, mat_2, mat_3 = 0, 0, 0
        while mat_1 == mat_2 or mat_2 == mat_3 or mat_3 == mat_1:
            mat_1, mat_2, mat_3 = np.random.choice(len(matches), 3)
        mat_1, mat_2, mat_3 = matches[mat_1], matches[mat_2], matches[mat_3]
        src, dst = [], []
        src.append(features1[mat_1[0]])
        src.append(features1[mat_2[0]])
        src.append(features1[mat_3[0]])
        dst.append(features2[mat_1[1]])
        dst.append(features2[mat_2[1]])
        dst.append(features2[mat_3[1]])
        matrix = get_affine_trans(src, dst)
        if matrix is None:
            continue
        rat = evaluate(matches, features1, features2, matrix)
        if rat > max_rat:
            max_rat = rat
            max_mat = matrix.copy()
    print max_rat
    return matrix

def visualize_ransac(matrix, matches, coords1, coords2, img1, img2, thres=10, show=False):
    img_h = max(img1.shape[0], img2.shape[0])
    img_w = img1.shape[1] + img2.shape[1]
    out = np.zeros((img_h, img_w, 3), dtype=img1.dtype)
    out[0 : img1.shape[0], : img1.shape[1], :] = img1
    out[0 : img2.shape[0], img1.shape[1] :, :] = img2
    for m_1, m_2 in matches:
        h_1, w_1 = coords1[m_1]
        h_2, w_2 = coords2[m_2]
        e_h, e_w = forward([h_1, w_1], matrix)
        color = (255, 0, 0)
        if abs(e_h - h_2) > thres or abs(e_w - w_2) > thres:
            color = (0, 0, 255)
        w_2 += img1.shape[1]
        cv2.circle(out, (w_1, h_1), 2, (0, 255, 0), 2)
        cv2.circle(out, (w_2, h_2), 2, (0, 255, 0), 2)
        cv2.line(out, (w_1, h_1), (w_2, h_2), color, 2)
    if show:
        visualize.show_bgr(out)
    else:
        return out

def compute_affine_xform(matches,features1,features2,image1,image2):
    """
    Computer Vision 600.461/661 Assignment 2
    Args:
        matches (list of tuples): list of index pairs of possible matches. For example, if the 4-th feature in feature_coords1 and the 0-th feature
                                  in feature_coords2 are determined to be matches, the list should contain (4,0).
        features1 (list of tuples) : list of feature coordinates corresponding to image1
        features2 (list of tuples) : list of feature coordinates corresponding to image2
        image1 (numpy.ndarray): The input image corresponding to features_coords1
        image2 (numpy.ndarray): The input image corresponding to features_coords2
    Returns:
        affine_xform (numpy.ndarray): a 3x3 Affine transformation matrix between the two images, computed using the matches.
    """

    affine_xform = ransac(matches, features1, features2)

    return affine_xform
