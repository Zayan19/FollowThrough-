from collections import deque
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
# import numpy as np
from PyQt4 import QtGui, QtCore

import argparse
import cv2
import imutils
import math

class Ball_Tracker():
    """
        Wrapper for implementing Ball tracking algorithms
        Currently self contained to start and stop OpenCV capturing
    """

    def __init__(self, is_live, video_path = None):
        self.is_live = is_live
        self.video_path = video_path

        if not self.is_live:
            if self.video_path is None or len(self.video_path) == 0:
                assert False, "Must supply a video if not using webcam"

        if is_live:
            self.camera = cv2.VideoCapture(0)
        else:
            self.camera = cv2.VideoCapture(self.video_path)

        self.theta = 0
        self.entryAngle = 0
        self.exitAngle = 0
        self.foundAngle = False

        # define the lower and upper boundaries of the "orange"
        # ball in the HSV color space, then initialize the
        # list of tracked points
        self.orangeLower = (3,100,160)
        self.orangeUpper = (10,180,240)


    def _clean_up(self):
        """ cleanup the camera and close any open windows """
        self.camera.release()
        cv2.destroyAllWindows()


    def begin_capture(self):
        pts = []
        #counter to check how many times the points have gone in the down and left self.direction
        downLeft = 0
        upLeft =0
        # upleftX;
        # upleftY;

        #initialize maxX,maxY values which represent the apex of the ball arc
        maxX=800
        maxY=800

        # keep looping
        while True:
            # grab the current frame
            (grabbed, frame) = self.camera.read()
            if not self.is_live and not grabbed:
                break

            # resize the frame, blur it, and convert it to the HSV
            # color space
            frame = imutils.resize(frame, width=900)
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # construct a mask for the color "green", then perform
            # a series of dilations and erosions to remove any small
            # blobs left in the mask
            mask = cv2.inRange(hsv, self.orangeLower, self.orangeUpper)
            mask = cv2.erode(mask, None, iterations=2)

            mask = cv2.dilate(mask, None, iterations=2)

            # find contours in the mask and initialize the current
            # (x, y) center of the ball
            cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE)[-2]
            center = None

            # only proceed if at least one contour was found
            if len(cnts) > 0:
                # find the largest contour in the mask, then use
                # it to compute the minimum enclosing circle and
                # centroid
                c = max(cnts, key=cv2.contourArea)
                ((x, y), radius) = cv2.minEnclosingCircle(c);
                # ((x2, y2), radius) = cv2.minEnclosingCircle(c);

                M = cv2.moments(c)
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

                # only proceed if the radius meets a minimum size
                if radius > 40:
                    # draw the circle and centroid on the frame,
                    # then update the list of tracked points
                    cv2.circle(frame, (int(x), int(y)), int(radius),
                        (0, 255, 255), 2)
                    cv2.circle(frame, center, 5, (0, 0, 255), -1)
                # update the points queue
                pts.append(center)

                # Find the max height of the ball
                if (y<maxY):
                    maxY=y
                    maxX=x

                length = len(pts) -1
                if length>=5:
                # Check to make sure it's going down left for a decent amount of time before computing the angle
                    if   self.direction(pts,1,5) and (self.direction(pts,2,5)) and not (self.direction(pts,0,5)) and not (self.direction(pts,3,5)):
                        downLeft = downLeft+1
                if (length >=5):
                    if downLeft >=5 and self.direction(pts,1,5) and (self.direction(pts,2,5)) and not (self.direction(pts,0,5)) and not (self.direction(pts,3,5)):
                        self.entryAngle = self.angle(x,y,maxX,maxY)
                        self.foundAngle = True

                print ("This is x",x,"This is y",y)
                length = len(pts) -1
                if length>=5:
                    # Check to make sure it's going up left for a decent amount of time before computing the angle
                    if  not self.direction(pts,1,5) and not (self.direction(pts,3,5)) and (self.direction(pts,0,5)) and (self.direction(pts,2,5)):
                        upLeft = upLeft+1
                if (length >=5):
                    if upLeft >=5 and not self.direction(pts,1,5) and not (self.direction(pts,3,5)) and (self.direction(pts,0,5)) and (self.direction(pts,2,5)):
                        print (x,y);
                        self.exitAngle = self.angle(x,y,585,298)
                        self.foundAngle = True


            #Once the angle is found, print it on screen
            if (self.foundAngle):
                cv2.putText(frame,"Entry angle is "+str(int(self.entryAngle))+" degrees!",(10,25),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3,0)
                cv2.putText(frame,"Exit angle is "+str(int(self.exitAngle))+" degrees!",(10,75),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3,0)
                cv2.putText(frame,"Max height was "+str(round(((250-maxY)/40),2))+" M!",(10,125),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3,0)

            # loop over the set of tracked points
            for i in range(1, len(pts)):
                # if either of the tracked points are None, ignore
                # them
                if pts[i - 1] is None or pts[i] is None:
                    continue
                # otherwise, compute the thickness of the line and
                # draw the connecting lines
                # thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
                cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), 2)

            # show the frame to our screen
            cv2.moveWindow("Frame", 0, 0)
            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('p'):
                while True:
                    if cv2.waitKey(1) == ord('p'):
                        break
            # if the 'q' key is pressed, stop the loop
            if key == ord("q"):
                break




        self._clean_up()

        maxY = round((250-maxY)/40,2)

        # valueList = [self.entryAngle,self.exitAngle,maxY]
        # return valueList;

    def direction (self, pts, direction = 0, frames = 3):
        # The return variable
        valueList = []
        isMovingInDirection = False
        length = len(pts) -1
        for i in range (frames, 0, -1):
            # Up
            if (self.direction == 0):
                if (pts[length - i][1] - pts[length - i +1][1] > 1):
                    isMovingInDirection = isMovingInDirection or True
            # Down
            elif (self.direction == 1):
                if (pts[length - i][1] - pts[length - i +1][1] < 1):
                    isMovingInDirection = isMovingInDirection or True
            # Down
            elif (self.direction == 2):
                if (pts[length - i][0] - pts[length - i +1][0] > 1):
                    isMovingInDirection = isMovingInDirection or True
            # Down
            elif (self.direction == 3):
                if (pts[length - i][0] - pts[length - i +1][0] < 1):
                    isMovingInDirection = isMovingInDirection or True
        return isMovingInDirection

    def angle(self, cx, cy, ex, ey) :
       dy = ey - cy;
       dx = ex - cx;
       self.theta = math.atan2(dy, dx);
       # // range (-PI, PI]
       self.theta *= (180 / math.pi);
       self.theta = abs(self.theta)
       # self.theta=180-self.theta
       return self.theta

if __name__=='__main__':
    Ball_Tracker(False, 'test_videos/FT_make.MOV').begin_capture()
