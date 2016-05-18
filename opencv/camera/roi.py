import site
site.addsitedir("/usr/local/lib/python2.7/site-packages")

import cv2
import numpy as np

def roiImage(cam):
  rval, frame = cam.read()
  frame = frame[140:1140, 0:800]
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  return rval, frame

cam = cv2.VideoCapture("testMovie.mp4")
backgroundImg = cv2.imread("background_1.png")
backgroundImg = cv2.cvtColor(backgroundImg,cv2.COLOR_BGR2GRAY)

rval, frame = roiImage(cam)

avg = np.float32(backgroundImg)
dif = cv2.absdiff(backgroundImg, frame)
difavg = np.float32(dif)
#cv2.accumulateWeighted(backgroundImg, avg, 0.01)
count = 0 
wg = 0.01

for idx in range(100):
  rval, frame = roiImage(cam)
  cv2.accumulateWeighted(frame, avg, wg)

while(rval):

  count += 1
  rval, frame = roiImage(cam) 

  cv2.accumulateWeighted(frame, avg, wg)
  res = cv2.convertScaleAbs(avg)

  dif = cv2.absdiff(res, frame)
  cv2.accumulateWeighted(dif, difavg, wg)

  difres = cv2.convertScaleAbs(difavg)

  cars = cv2.absdiff(dif,difres )

  ret, cars = cv2.threshold(cars, 50,255,cv2.THRESH_BINARY)

  #b,g,r = cv2.split(cars)

  #th = 50 
  #ret, b_th = cv2.threshold(b,th,255,cv2.THRESH_BINARY)
  #ret, g_th = cv2.threshold(g,th,255,cv2.THRESH_BINARY)
  #ret, r_th = cv2.threshold(r,th,255,cv2.THRESH_BINARY)

  #img = cv2.merge((b_th, g_th, r_th))
  #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  cv2.imshow('img',cars)

  k = cv2.waitKey(10)
  
