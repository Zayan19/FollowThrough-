import numpy as np
import cv2

ball = cv2.CascadeClassifier('ball_classifier.xml')


cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    balls = ball.detectMultiScale(gray, 50, 50)
    
    # add this
    for (x,y,w,h) in balls:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
