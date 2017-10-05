import cv2
import numpy
import matplotlib.pyplot as plt

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
	
    descriptors = dict()

    return descriptors
