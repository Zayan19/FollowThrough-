import cv2
import numpy as np

# Bring the haar cascade file into python
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Begin capuring using default camera
cap = cv2.VideoCapture(0)

while True:
    # read in what the webcam is capturing (we don't care about the first thing cap.read() returns, hence the _)
    _, img = cap.read()
    # Convert the image to grayscale for easier detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Use the cascade file to detect all the faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        # Draw a 2px wide blue rectangle around all the faces in the video
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)


    # Show the stream using opencv
    cv2.imshow('img', img)

    # If you press q, quit everything
    k = cv2.waitKey(30) & 0xFF
    if k == ord('q'):
        break

# Release the webcam
cap.release()
cv2.destroyAllWindows()
