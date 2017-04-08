import cv2
import numpy as np

class Ball_Detector(object):

    def __init__(self, haarFile):
        # if haarFile is None, implementing hard coded tests!
        if haarFile is None:
            self._object = None
        else:
            self._object = cv2.CascadeClassifier(haarFile)

    def find_object(self, frame):
        if self._object is None:
            # Hard coded tests!
            return (1070, 570, 50, 50)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        points = self._object.detectMultiScale(gray, 1.3, 5)

        if points is None or len(points) == 0:
            return False
        else:
            return points

