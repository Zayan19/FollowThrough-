

import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import numpy as np
from managers import WindowManager, CaptureManager
from Ball_Detector import Ball_Detector
import math

def direction2(x,y,x2,y2,directionCheck):
    if (directionCheck =="upright"):
        if (x2<x and y2<y):
            return True


    if (directionCheck =="downright"):
        if (x2<x and y2>y):
            return True

    if (directionCheck =="upleft"):
        if (x2>x and y2<y):
            return True

    if (directionCheck =="downleft"):
        if (x2>x and y2>y):
            return True
    return False


def angle(cx, cy, ex, ey) :
    dy = ey - cy;
    dx = ex - cx;
    global theta
    theta = math.atan2(dy, dx);
    # // range (-PI, PI]
    theta *= (180 / math.pi);
    theta = abs(theta)
    # theta=180-theta
    return int(round(theta))

class Ball_Tracker(object):

    def __init__(self, windowName, capture):
        self._windowManager = WindowManager(windowName, self.onKeypress)
        self._captureManager = CaptureManager(capture, self._windowManager, True)
        self._ball_detector = Ball_Detector("ball_classifier.xml")

        # define a geneal orange color to help with detection
        self.orangeLower = (0,96,91)
        self.orangeUpper = (7,255,255)



    def run(self):

        exitAngle = 0
        entryAngle =0
        upRight=0
        downRight=0


        foundEntryAngle=False
        foundExitAngle =False
        #initialize maxX,maxY values which represent the apex of the ball arc
        maxX=800
        maxY=800

        counter = 50

        xCoord2 = 0
        yCoord2 = 0
        self._windowManager.createWindow()

        # Find object coordinates using HaarCascade
        track_window = self._find_basketball()

        # Grab the next frame of the video to initialize tracking
        self._captureManager.enterFrame()
        frame = self._captureManager.frame
        self._captureManager.exitFrame()

        # Set up what is needed for the meanShift tracking
        hsv_roi = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_roi, self.orangeLower, self.orangeUpper)

        roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0,180])
        cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

        term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)


        while self._windowManager.isWindowCreated:
            # Grab the next frame from the video
            entered = self._captureManager.enterFrame()

            if not entered:
                break
            frame = self._captureManager.frame

            # convert the current frame to HSV color space for back_projection calculation
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            back_project = cv2.calcBackProject([hsv], [0], roi_hist, [0,180], 1)

            # Mean Shift. Returns the updated location of the object
            ret, track_window = cv2.meanShift(back_project, track_window, term_crit)
            (x,y,w,h) = track_window

            # Draw a rectangle around the ball
            cv2.rectangle(frame, (x,y), (x+w, y+h), 255, 2)

            #get the x and y coordinates of the ball
            xCoord = x+x+w/2
            yCoord = y+y+h/2

            # print ("This is xCoord and yCoord",xCoord,yCoord)
            # print ("This is xCoord2 and yCoord2",xCoord2,yCoord2)

            counter-=1
            if (counter==0):
                counter = 50
                xCoord2 = x+x+w/2
                yCoord2 = y+y+h/2
                # print("Updated")

            if (direction2(xCoord2,yCoord2,xCoord,yCoord,"upright")==True):
                # print("It's working!!!")
                upRight+=1


            if (upRight>5 and foundExitAngle==False):
                foundExitAngle=True
                exitAngle=angle(xCoord,yCoord,2074,800)
                print("The exit angle was",exitAngle)


            if (direction2(xCoord,yCoord,xCoord2,yCoord2,"downright")==True):
                # print("It's working!!!")
                downRight+=1


            if (downRight>5 and foundEntryAngle==False):
                foundEntryAngle=True
                entryAngle=angle(xCoord,yCoord,maxX,maxY)
                print "The entry angle was",entryAngle
                print "The ball's max height was:",1000-maxY, "units."




            # Find the max height of the ball
            if (maxY>yCoord):
                maxY=y
                maxX=x


            # Set the frame to be displayed
            self._captureManager.frame = frame


            # Signal we are done with the frame, write to cv2.imshow
            self._captureManager.exitFrame()

            # Always listen for specific keypress events
            # Triggered by onKeypress(keycode)!
            self._windowManager.processEvents()


    def _find_basketball(self):
        while True:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame

            track_window = self._ball_detector.find_object(frame)
            if track_window is not False:
                self._captureManager.exitFrame()
                break

            self._captureManager.exitFrame()
        return track_window


    def onKeypress(self, keycode):
        """
            Handle a keypress

            space -> Take a screenshot
            tab -> start / stop recording a screencast
            esc -> quit
        """
        # spacebar
        if keycode == 32:
            self._captureManager.writeImage('screenshot.png')
        # tab
        elif keycode == 9:
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo('screencast.avi')
            else:
                self._captureManager.stopWritingVideo()
        # esc
        elif keycode == 27:
            self._windowManager.destroyWindow()

if __name__ == '__main__':
   Ball_Tracker('Ball Tracker', cv2.VideoCapture('test_videos/3P_make.MOV')).run()
