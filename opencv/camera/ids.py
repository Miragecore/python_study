import site
site.addsitedir("/usr/local/lib/python2.7/site-packages")
import cv2
import numpy as np


def splitShow(img):
  b,g,r = cv2.split(img)
  
  cv2.imshow('b',b)
  cv2.imshow('g',g)
  cv2.imshow('r',r)

def ROIShow(img, x,y,width,height,isShow=False):
  roi = img[y:y+height, x:x+width]
  if isShow:
    cv2.imshow('roi',roi)
  return roi

def ReadGray(fileName):
  img = cv2.imread(fileName)
  img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  return img

def ReadRed(fileName):
  img = cv2.imread(fileName)
  b,g,r = cv2.split(img)
  return r

def GetMatchTopLeft(img, template):
  res = cv2.matchTemplate(ids_img,info_tag,cv2.TM_CCOEFF)
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

  top_left = max_loc
  return res, top_left

def GetInfoTagPos(img, template):
  res, tl = GetMatchTopLeft(img, template) 
  w, h = template.shape[::-1]
  top_left = (tl[0] + w-2, tl[1] -10)
  btm_right = (top_left[0] + 227, top_left[1] + 120)
  return top_left, btm_right

def GetInfoTagROI(img, template):
  tl, br = GetInfoTagPos(img, template)
  #roi = img[tl[1]:br[1], tl[0]:br[0]]
  roi = img[tl[1]:(tl[1]+br[1])/2, tl[0]:br[0]]
  return roi

def dilate(img):
  ret = img
  kernel = np.ones((2,2),np.uint8)
  #kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
  #kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
  #for i in range(1):
  ret = cv2.dilate(ret, kernel, 1)
  #ret = cv2.erode(ret, kernel, 1)

  return ret

#img = cv2.imread('ids.png')
#tmp = cv2.imread('stopletter.tiff')
#tmp = tmp[4:25,0:19]
#cv2.imshow('tmp', tmp)
#splitShow(img)

info_tag = ReadRed('info_tag.png')
ids_img = ReadRed('ids.png')
#327, 119
#tl, br = GetInfoTag(ids_img, info_tag)

#cv2.rectangle(ids_img, tl, br, 255,2)
#info_plate = ids_img[tl[1]:br[1], tl[0]:br[0]]
info_plate = GetInfoTagROI(ids_img, info_tag)
ret, info_plate = cv2.threshold(info_plate, 127,
                                255, 
                                cv2.THRESH_BINARY_INV)

#info_plate = dilate(info_plate)
w,h = info_plate.shape[::-1]
emptyline = 0
for idx in range(h):
  line = info_plate[idx:idx+1,0:]
  print line
  if (cv2.countNonZero(line) == w-1):
    continue
  
  if (cv2.countNonZero(line) == w) :
    emptyline = idx
    break

print emptyline

cv2.imshow('plate',info_plate)
cv2.imwrite('plate.tif',info_plate)
#cv2.imshow('img',ids_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
