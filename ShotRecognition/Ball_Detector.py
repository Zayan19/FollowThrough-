import cv2
import numpy as np

class Ball_Detector(object):

    def __init__(self, haarFile):
        # if haarFile is None, implementing hard coded tests!
        self._object = cv2.CascadeClassifier(haarFile)
        # define a geneal orange color to help with detection
        self.orangeLower = (0,96,91)
        self.orangeUpper = (7,255,255)

    def find_object(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        points = self._object.detectMultiScale(gray, 50, 50)

        if points is None or len(points) == 0:
            return False
        else:
            mask_filter = []
            for (x,y,w,h) in points:
                roi = frame[y:y+h, x:x+w]
                hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
                mask = cv2.inRange(hsv, self.orangeLower, self.orangeUpper)
                count = np.count_nonzero(mask)

                mask_filter.append(count)

            max_points = max(mask_filter)
            probable_ball_index = mask_filter.index(max_points)
            x = points[probable_ball_index][0]
            y = points[probable_ball_index][1]
            w = points[probable_ball_index][2]
            h = points[probable_ball_index][3]
            if max_points < 150:
                return False
            return (x,y,w,h)


                


