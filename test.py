import math
def angle(cx, cy, ex, ey) :
   dy = ey - cy;
   dx = ex - cx;
   theta = math.atan2(dy, dx);
   # // range (-PI, PI]
   global theta
   theta *= 180 / math.pi;
   theta = 180 - theta
   # // rads to degs, range (-180, 180]
  # //if (theta < 0) theta = 360 + theta; // range [0, 360)
   # cv2.putText(frame,str(int(theta)), (50,70), cv2.FONT_HERSHEY_SIMPLEX, 3,(255,0,0),4, 0)
   # cv2.putText(frame,'Hello World!',(10,500), font, 1,(255,255,255),2)
   print ("This is the angle: ", theta);
   return theta

# ('This is x', 216.5, 'This is y', 139.0)
# ('This is x2', 285.0, 'This is y', 93.0)

angle(413,133.5,165,174)
