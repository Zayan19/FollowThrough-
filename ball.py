
from collections import deque
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
# import numpy as np
import argparse
import cv2
import imutils
import math



def direction (pts, direction = 0, frames = 3):
    # The return variable
    valueList = []
    isMovingInDirection = False
    length = len(pts) -1
    for i in range (frames, 0, -1):
        # Up
        if (direction == 0):
            if (pts[length - i][1] - pts[length - i +1][1] > 1):
                isMovingInDirection = isMovingInDirection or True
        # Down
        elif (direction == 1):
            if (pts[length - i][1] - pts[length - i +1][1] < 1):
                isMovingInDirection = isMovingInDirection or True
        # Down
        elif (direction == 2):
            if (pts[length - i][0] - pts[length - i +1][0] > 1):
                isMovingInDirection = isMovingInDirection or True
        # Down
        elif (direction == 3):
            if (pts[length - i][0] - pts[length - i +1][0] < 1):
                isMovingInDirection = isMovingInDirection or True
    return isMovingInDirection

def angle(cx, cy, ex, ey) :
   dy = ey - cy;
   dx = ex - cx;
   global theta
   theta = math.atan2(dy, dx);
   # // range (-PI, PI]
   theta *= (180 / math.pi);
   theta = abs(theta)
   # theta=180-theta
   return theta


def runVideo(stream, video_path=None):

    if (not stream and video_path is None):
        print("Must supply a video if not streaming")
        return

    theta = 0
    entryAngle = 0
    exitAngle = 0
    foundAngle = False
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-b", "--buffer", type=int, default=15,
        help="max buffer size")
    args = vars(ap.parse_args())

    # define the lower and upper boundaries of the "orange"
    # ball in the HSV color space, then initialize the
    # list of tracked points
    orangeLower = (3,100,160)
    orangeUpper = (10,180,240)

    pts = []

    # If user wants to stream 
    if stream:
        camera = cv2.VideoCapture(0)
    # Otherwise, use 
    else:
        camera = cv2.VideoCapture(video_path)

    #counter to check how many times the points have gone in the down and left direction
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
        (grabbed, frame) = camera.read()

        # if we are viewing a video and we did not grab a frame,
        # then we have reached the end of the video
        if not stream and not grabbed:
            break

        # resize the frame, blur it, and convert it to the HSV
        # color space
        frame = imutils.resize(frame, width=900)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # construct a mask for the color "green", then perform
        # a series of dilations and erosions to remove any small
        # blobs left in the mask
        mask = cv2.inRange(hsv, orangeLower, orangeUpper)
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
                if   direction(pts,1,5) and (direction(pts,2,5)) and not (direction(pts,0,5)) and not (direction(pts,3,5)):
                    downLeft = downLeft+1
            if (length >=5):
                if downLeft >=5 and direction(pts,1,5) and (direction(pts,2,5)) and not (direction(pts,0,5)) and not (direction(pts,3,5)):
                    entryAngle = angle(x,y,maxX,maxY)
                    foundAngle = True

            print ("This is x",x,"This is y",y)
            length = len(pts) -1
            if length>=5:
                # Check to make sure it's going up left for a decent amount of time before computing the angle
                if  not direction(pts,1,5) and not (direction(pts,3,5)) and (direction(pts,0,5)) and (direction(pts,2,5)):
                    upLeft = upLeft+1
            if (length >=5):
                if upLeft >=5 and not direction(pts,1,5) and not (direction(pts,3,5)) and (direction(pts,0,5)) and (direction(pts,2,5)):
                    print (x,y);
                    exitAngle = angle(x,y,585,298)
                    foundAngle = True




        # Determine direction of ball
        # Confirm there are at least 10 points before trackign starts
        # length = len(pts) - 1
        # if (length >= 10):
        #   if(direction(pts, 0, 5)):
        #       cv2.putText(frame,"U", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 0)
        #   if(direction(pts, 1, 5)):
        #       cv2.putText(frame,"D", (100,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 0)
        #   if(direction(pts, 2, 5)):
        #       cv2.putText(frame,"L", (150,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 0)
        #   if(direction(pts, 3, 5)):
        #       cv2.putText(frame,"R", (200,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 0)

        #Once the angle is found, print it on screen
        if (foundAngle):
            cv2.putText(frame,"Entry angle is "+str(int(entryAngle))+" degrees!",(10,25),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3,0)
            cv2.putText(frame,"Exit angle is "+str(int(exitAngle))+" degrees!",(10,75),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3,0)
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




    # cleanup the camera and close any open windows
    camera.release()
    cv2.destroyAllWindows()
    maxY = round((250-maxY)/40,2)

    valueList = [entryAngle,exitAngle,maxY]
    return valueList;


if __name__ == '__main__':
    runVideo(False, 'test_videos/FT_make.MOV')
