from collections import deque
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import numpy as np
import argparse
import cv2
import imutils
import math



# takes a Direction (tuple list, integer (0-3), int frames)
# tuple is a list of points that the ball has last travelled
# 0 = up, 1 = down, 2 = left, 3 = right
def direction (pts, direction = 0, frames = 3):
	# The return variable
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
   theta = math.atan2(dy, dx);
   # // range (-PI, PI]
   theta *= 180 / math.pi;
   # // rads to degs, range (-180, 180]
  # //if (theta < 0) theta = 360 + theta; // range [0, 360)
   cv2.putText(frame,str(theta), (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 0)
   print ("This is the angle: ", theta);


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
# ap.add_argument("-v", "--video","--/home/zack/Uni/Capstone/ball-tracking/FT_make.MOV")
ap.add_argument("-b", "--buffer", type=int, default=15,
	help="max buffer size")
args = vars(ap.parse_args())

# define the lower and upper boundaries of the "green"
# ball in the HSV color space, then initialize the
# list of tracked points
blueLower = (110,50,50)
blueUpper = (130,255,255)
# greenLower = (0, 150, 155)
# greenUpper = (248, 255, 255)
# orange water bottle cap
greenLower = (0,86,211)
greenUpper = (8,255,255)
orangeLower = (3,100,160)
orangeUpper = (10,180,240)

# greenLower = (29, 86, 6)
# greenUpper = (64, 255, 255)
pts = []
# ([17, 15, 100], [50, 56, 200]),
# if a video path was not supplied, grab the reference
# to the webcam
# if not args.get("video", False):

#if True then it runs your native camera, otherwise the specified video
if False:
	camera = cv2.VideoCapture(0)
# otherwise, grab a reference to the video file
else:
	camera = cv2.VideoCapture("test_videos/FT_miss_2.MOV")

# keep looping
counter = 100
x2 = 0
y2 = 0
while True:
	# grab the current frame
	(grabbed, frame) = camera.read()

	# if we are viewing a video and we did not grab a frame,
	# then we have reached the end of the video
	if args.get("video") and not grabbed:
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
        #print out the x and y coordinates
		print ("This is x",x,"This is y",y)
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
        if  counter<0:
            ((x2, y2), radius) = cv2.minEnclosingCircle(c);
            counter= 1000
        counter = counter -1
        angle(x,y,x2,y2)

	# Determine direction of ball
	# Confirm there are at least 10 points before trackign starts
	length = len(pts) - 1
	if (length >= 10):
		# Is it moving up?

		if(direction(pts, 0, 5)):
			cv2.putText(frame,"U", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 0)
		if(direction(pts, 1, 5)):
			cv2.putText(frame,"D", (100,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 0)
		if(direction(pts, 2, 5)):
			cv2.putText(frame,"L", (150,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 0)
		if(direction(pts, 3, 5)):
			cv2.putText(frame,"R", (200,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 0)

	# loop over the set of tracked points
	for i in xrange(1, len(pts)):
		# if either of the tracked points are None, ignore
		# them
		if pts[i - 1] is None or pts[i] is None:
			continue
		# otherwise, compute the thickness of the line and
		# draw the connecting lines
		# thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
		cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), 2)


	# show the frame to our screen
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
