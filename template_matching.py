#####################################################################################
#                           Template Matching using OpenCV
#####################################################################################

import cv2
import numpy as np
from matplotlib import pyplot as plt

def MatchTemplate(image, width, height, car):
    # three different methods used for template matching
    template_methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED','cv2.TM_CCORR_NORMED']

    for m in template_methods:
        image_copy = image.copy()
        method = eval(m)

        res = cv2.matchTemplate(image_copy, car, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        cv2.rectangle(image_copy, max_loc, (max_loc[0] + width, max_loc[1] + height), 255, 3)

        plt.subplot(121),plt.imshow(res,cmap = 'gray')
        plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(image_copy,cmap = 'gray')
        plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
        plt.suptitle(m)

        plt.show()


image = cv2.imread("solidWhiteCurve.jpg", 0)
car = image[297:359, 190:278]
width, height = car.shape[::-1]
MatchTemplate(image, width, height, car)
