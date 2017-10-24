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
    g = sp.Symbol('g')
    h = sp.Symbol('h')
    t = []
    t.append(sp.Symbol('t0'))
    t.append(sp.Symbol('t1'))
    t.append(sp.Symbol('t2'))
    t.append(sp.Symbol('t3'))
    eq_list = []
    sm_list = [a, b, c, d, e, f, g, h, t[0], t[1], t[2], t[3]]
    for idx in range(4):
        eq_list.append(sp.Eq(a * src[idx][1] + b * src[idx][0] + c, dst[idx][1] * t[idx]))
        eq_list.append(sp.Eq(d * src[idx][1] + e * src[idx][0] + f, dst[idx][0] * t[idx]))
        eq_list.append(sp.Eq(g * src[idx][1] + h * src[idx][0] + 1, t[idx]))
    solution = sp.solve(eq_list, sm_list)
    try:
        affine_xform = np.zeros((3, 3))
        affine_xform[0][0] = float(solution[a])
        affine_xform[0][1] = float(solution[b])
        affine_xform[0][2] = float(solution[c])
        affine_xform[1][0] = float(solution[d])
        affine_xform[1][1] = float(solution[e])
        affine_xform[1][2] = float(solution[f])
        affine_xform[2][0] = float(solution[g])
        affine_xform[2][1] = float(solution[h])
        affine_xform[2][2] = 1
        return affine_xform
    except:
        return None

def forward(src, mat):
    x = mat[0][0] * src[1] + mat[0][1] * src[0] + mat[0][2]
    y = mat[1][0] * src[1] + mat[1][1] * src[0] + mat[1][2]
    z = mat[2][0] * src[1] + mat[2][1] * src[0] + mat[2][2]
    if z == 0:
        return [0.0, 0.0]
    return [y / z, x / z]

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

def ransac(matches, features1, features2, thres, ran_round=200):
    if len(matches) < 4:
        return None
    max_rat, max_mat = 0.0, None
    for ran_idx in range(ran_round):
        mat_1, mat_2, mat_3, mat_4 = 0, 0, 0, 0
        while mat_1 == mat_2 or mat_1 == mat_3 or mat_1 == mat_4 or \
              mat_2 == mat_3 or mat_2 == mat_4 or mat_3 == mat_4:
            mat_1, mat_2, mat_3, mat_4 = np.random.choice(len(matches), 4)
        mat_1, mat_2 = matches[mat_1], matches[mat_2]
        mat_3, mat_4 = matches[mat_3], matches[mat_4]
        src, dst = [], []
        src.append(features1[mat_1[0]])
        src.append(features1[mat_2[0]])
        src.append(features1[mat_3[0]])
        src.append(features1[mat_4[0]])
        dst.append(features2[mat_1[1]])
        dst.append(features2[mat_2[1]])
        dst.append(features2[mat_3[1]])
        dst.append(features2[mat_4[1]])
        matrix = get_affine_trans(src, dst)
        if matrix is None:
            continue
        rat = evaluate(matches, features1, features2, matrix, thres)
        if rat > max_rat:
            max_rat = rat
            max_mat = matrix.copy()
    return max_mat

def visualize_ransac(matrix, matches, coords1, coords2, img1, img2, show=False):
    thres = max(img1.shape[0] / 20, 1)
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

def compute_proj_xform(matches,features1,features2,image1,image2):
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
        proj_xform (numpy.ndarray): a 3x3 Projective transformation matrix between the two images, computed using the matches.
    """
    np.random.seed(1)
    thres = max(image1.shape[0] / 20, 1)
    proj_xform = ransac(matches, features1, features2, thres)

    return proj_xform
