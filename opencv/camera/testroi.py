import site
site.addsitedir("/usr/local/lib/python2.7/site-packages")
import cv2
import numpy as np

c = cv2.VideoCapture("testVideo.mp4")
#c = cv2.VideoCapture(0)

rval, frame = c.read()
roi = frame[300:310, 250:350]

avg = np.float32(roi)
count = 0;
while(rval):
  rval, frame = c.read()
  count += 1
  roi = frame[300:310, 250:350]

  cv2.accumulateWeighted(roi, avg, 0.005)
  #cv2.accumulate(frame,avg);
  #avg /= count

  res = cv2.convertScaleAbs(avg)

  dif = cv2.absdiff(res,roi)
  b,g,r = cv2.split(dif)

  th = 50 
  ret, b_th = cv2.threshold(b,th,255,cv2.THRESH_BINARY)
  ret, g_th = cv2.threshold(g,th,255,cv2.THRESH_BINARY)
  ret, r_th = cv2.threshold(r,th,255,cv2.THRESH_BINARY)

  img = cv2.merge((b_th,g_th,r_th))
  #cv2.rectangle(img, (250,300), (350,310),(0,255,0),1)

  #if count > 100:
  #cv2.imshow('src', frame)
  cv2.imshow('avg', roi)
  #cv2.imshow('dif',dif)
  cv2.imshow('img',img)
  print count
    

  k = cv2.waitKey(10)

  if k == 27:
    break;

cv2.destroyAllWindows()
c.release()


