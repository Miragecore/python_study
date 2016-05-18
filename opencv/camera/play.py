import site
site.addsitedir("/usr/local/lib/python2.7/site-packages")

import cv2
import numpy as np

cam = cv2.VideoCapture("0328.mp4")

rval, frame = cam.read()

while(rval):
  imshow(frame)
  rval, frame = cam.read()

  k = cv2.waitKey(10)

  if k == 27:
    break

cv2.destroyAllWindows()
cam.release()

