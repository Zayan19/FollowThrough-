import sys
import math
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import numpy as np
from managers import WindowManager, CaptureManager
from Ball_Detector import Ball_Detector
from collections import deque

def direction2(x,y,x2,y2,directionCheck):
    """Direction function used to calculate which direction the ball is travelling.
    It takes in two pairs of coordinates to compare as well as the direction is being check.
    Outputs true if the direction being checked is found, false otherwise.
    """

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
    """Given two pairs of coordinates, outputs the angle between them"""
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
        """
        Constructor used to initialize the window manager, capture manager and ball detector
        Also initializes orangeLower and orangeUpper which is a range of orange values used to help with detection
        """
        self._windowManager = WindowManager(windowName, self.onKeypress)
        self._captureManager = CaptureManager(capture, self._windowManager, True)
        self._ball_detector = Ball_Detector("ball_classifier.xml")

        self._paused = False
        # define a geneal orange color to help with detection
        self.orangeLower = (0,96,91)
        self.orangeUpper = (7,255,255)

    def run(self):
        """
        Runs the main application. It performs the following actions:

        1. Initializes variables to store the current ball direction amount, the angles and the max height
        2. Sets up meanshift tracking for the basketball
        3. Computes end points of small line to check which direction the ball is moving.
        4. Computes angle between points.
        5. Computes the highest point reached.
        6. Continues to update the values frame by frame while the application is still running.
        7. Returns the entry Angle, maximum ball height and exit angle if found.
        8. Displays the corresponding values on screen.
        """

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

        # define list of points
        self.points = deque(maxlen=32)

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
            # Handle Video Pausing
            while self._paused:
                self._windowManager.processEvents()

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
                print( "The ball's max height was:",1000-maxY, "units." )
                foundEntryAngle=True
                entryAngle=angle(xCoord,yCoord,maxX,maxY)
                print( "The entry angle was",entryAngle )

            # Find the max height of the ball
            if (maxY>yCoord):
                maxY=y
                maxX=x

            self.points.appendleft( (int(x+w/2), int(y+h/2)) )

            # Draw a rectangle around the ball
            cv2.rectangle(frame, (x,y), (x+w, y+h), 255, 2)
            for i in range(1, len(self.points)):
                # if either of the tracked points are None, ignore
                # them
                if self.points[i - 1] is None or self.points[i] is None:
                    continue
                # otherwise, compute the thickness of the line and
                # draw the connecting lines
                thickness = int(np.sqrt(32 / float(i + 1)) * 2.5)
                cv2.line(frame, self.points[i - 1], self.points[i], (0, 0, 255), thickness)

            # Set the frame to be displayed
            self._captureManager.frame = frame

            if (foundExitAngle):
                cv2.putText(frame,"Entry angle was "+str(int(entryAngle))+" degrees!",(10,25),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3,0)
                cv2.putText(frame,"Exit angle was "+str(int(exitAngle))+" degrees!",(10,75),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3,0)
                cv2.putText(frame,"Max height was "+str((1000-maxY)/float(200))+" M!",(10,125),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3,0)
            # Signal we are done with the frame, write to cv2.imshow
            self._captureManager.exitFrame()

            # Always listen for specific keypress events
            # Triggered by onKeypress(keycode)!
            self._windowManager.processEvents()
            cv2.imshow("Frame", frame)


    def _find_basketball(self):
        """
        Attempt to find basketball on screen
        Returns tracked window if found

        """
        while True:
            entered = self._captureManager.enterFrame()
            frame = self._captureManager.frame

            track_window = self._ball_detector.find_object(frame)

            if not entered:
                break

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

        elif keycode == ord('p'):
            self._paused = not self._paused


if __name__ == '__main__':
   Ball_Tracker('Ball Tracker', cv2.VideoCapture('test_videos/3P_make.MOV')).run()
