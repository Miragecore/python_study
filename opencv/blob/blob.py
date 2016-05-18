import site
site.addsitedir("/usr/local/lib/python2.7/site-packages")

import numpy as np
import cv2
import disjoint as dj
from matplotlib import pyplot as plt

def CheckInImage(col, row):
    if col < 0 or row < 0 :
        return False

    return True

def GetLeft(image, col, row):
    col = col - 1
    
    if not CheckInImage(col, row) :
        return 0
    else :
        return image[row,col]

def GetNorth(image, col, row):
    row = row - 1
    if not CheckInImage(col, row) :
        return 0
    else :
        return image[row, col]


img = cv2.imread('test.jpg', cv2.IMREAD_UNCHANGED  )

height, width, channel = img.shape

print width, height, channel

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,thresh1 = cv2.threshold(gray_image,127,255,cv2.THRESH_BINARY)

lbl_image = np.zeros((height,width,1), np.uint16)
Dp_image = np.zeros((height,width,1), np.uint8)

#plt.imshow(img)
#plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
#plt.show()

#thresh1[100,100]
forest = dj.disjointForest()
index = 0

print 'start first pass'
for iRow in range(height):
    for iCol in range(width):
        #print iRow, iCol, thresh1[iRow, iCol]
        cpxl = thresh1[iRow,iCol]
        wpxl = GetLeft(thresh1, iCol, iRow)
        npxl = GetNorth(thresh1, iCol, iRow)
        if cpxl > 128 :
            if wpxl > 128 and npxl > 128 :
                lbl_image[iRow,iCol] = lbl_image[iRow,iCol-1]
                forest.MergeByLabel(int(lbl_image[iRow-1,iCol]),
                                    int(lbl_image[iRow, iCol-1]))
                ''' 
                witem = forest.GetItem(int(lbl_image[iRow-1,iCol]))
                nitem = forest.GetItem(int(lbl_image[iRow, iCol-1]))
                witem.Merge(nitem)                
                '''
            elif wpxl > 128 :
                lbl_image[iRow,iCol] = lbl_image[iRow,iCol-1]
            elif npxl > 128 :
                lbl_image[iRow,iCol] = lbl_image[iRow-1,iCol]               
            else :
                lbl_image[iRow,iCol] = index
                forest.AddItem(index)
                index = index + 1
                #print index
        elif wpxl > 128 and npxl > 128 :
            #print wpxl, npxl
            forest.MergeByLabel(int(lbl_image[iRow-1,iCol]),
                                int(lbl_image[iRow, iCol-1]))
            '''
            witem = forest.GetItem(int(lbl_image[iRow-1,iCol]))
            nitem = forest.GetItem(int(lbl_image[iRow, iCol-1]))
            witem.Merge(nitem)
            '''
            
print 'index : ', index

print 'start second pass '
maxRoot = 0
for iRow in range(height):
    for iCol in range(width):
        Dp_image[iRow,iCol] = forest.GetItem(int(lbl_image[iRow,iCol])).FindRoot().label
        if lbl_image[iRow,iCol] > maxRoot :
            maxRoot = lbl_image[iRow,iCol]

print 'MaxRoot : ', maxRoot

print 'end of pass'
        
'''
titles = ['Original Image','GRAY','label']
images = [img, gray_image, lbl_image]

for i in xrange(3):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
'''

cv2.imshow('image',Dp_image)
cv2.waitKey(0)
cv2.destroyAllwindow()
