import site
site.addsitedir("/usr/local/lib/python2.7/site-packages")
import cv2

cv2.namedWindow("preview")
vc = cv2.VideoCapture("rtsp://192.168.123.5:8554/ted")
if vc.isOpened():
  vc.grab()
  rval, frame = vc.read()
  print 'Opend'
else:
  rval = False
  print 'not opened'

while rval:
  cv2.imshow("preview", frame)
  rval, frame = vc.read()
  #cv2.arrowedLine(frame, (100,100),(100,200),(0,0,255),5)
  #fast = cv2.FastFeatureDetector()
  #kp = fast.detect(frame,None)

  #ORB
  orb= cv2.ORB()

  kp = orb.detect(frame, None)

  kp, des = orb.compute(frame, kp)

  frame = cv2.drawKeypoints(frame, kp, color=(255,0,0))

  key = cv2.waitKey(20)
  if key == 27:
    break

vc.release()
cv2.destroyWindow("preview")
