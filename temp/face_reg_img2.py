import tensorflow.compat.v1 as tf
import argparse
import facenet
import os
import sys
import math
import pickle
import numpy as np
import cv2
import collections
from sklearn.svm import SVC
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
import converter

class FaceRecog:
    def __init__(self):
        self.cropped = np.zeros((2, 2))
            


#test = FaceRecog()
