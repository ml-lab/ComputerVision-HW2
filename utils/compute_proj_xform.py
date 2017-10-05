# Author: TK
import cv2
import numpy
import matplotlib.pyplot as plt

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
    
    proj_xform = np.zeros((3,3))

    return proj_xform
