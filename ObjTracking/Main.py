from DetectedObject import *
from ReadData import ReadData
import matplotlib.pyplot as plt


import re

#logname = "log.09.36.txt"
logname = "log.15.40.txt" #RSU-08
#logname = "KumGangBr.txt"

pos_x = []
pos_y = []
short = [0.0, 0, 0.0 , 0.0] #Sum, Count Avg stdev
middle = [0.0, 0, 0.0, 0.0]
long = [0.0, 0, 0.0, 0.0]
#long-middle 674
#middle-shot 222
seq_dobjs = ReadData(logname)
for scene in seq_dobjs:
    for obj in scene:
        if obj.y <= 222 :
            short[0] += obj.x
            short[1] += 1
        if obj.y <= 674 and obj.y > 222:
            middle[0] += obj.x
            middle[1] += 1
        if obj.y > 674:
            long[0] += obj.x
            long[1] += 1

short[2] = short[0] / short[1]
middle[2] = middle[0] / middle[1]
long[2] = long[0] / long[1]

"""
#평규을 이용한 쉬프트
for scene in seq_dobjs:
    for obj in scene:
        if obj.y <= 222:
            obj.x -= short[2]
        if obj.y <= 674 and obj.y > 222:
            obj.x -= middle[2]
        if obj.y > 674:
            obj.x -= long[2]

        pos_x.append(obj.x)
        pos_y.append(obj.y)
"""

for scene in seq_dobjs:
    for obj in scene:
        if obj.y <= 222 :
            short[3] += math.pow((short[2] - obj.x), 2)
        if obj.y <= 674 and obj.y > 222:
            middle[3] += math.pow((middle[2] - obj.x), 2)
        if obj.y > 674:
            long[3] += math.pow((long[2] - obj.x), 2)


short[3] = math.sqrt(short[3]/short[1])
middle[3] = math.sqrt(middle[3]/middle[1])
long[3] = math.sqrt(long[3]/middle[1])
print("std")
print(short[3])
print(middle[3])
print(long[3])

shortxrange = [0.0, 0.0]
middlexrange = [0.0, 0.0]
longxrange = [0.0, 0.0]

shortxrange[0] = short[2] - short[3] * 3
shortxrange[1] = short[2] + short[3] * 3

middlexrange[0] = middle[2] - middle[3] * 3
middlexrange[1] = middle[2] + middle[3] * 3

longxrange[0] = long[2] - long[3] * 3
longxrange[1] = long[2] + long[3] * 3

print("range")
print("short {0} {1}, middle {2} {3}, long {4} {5}".format(shortxrange[0], shortxrange[1], middlexrange[0], middlexrange[1],longxrange[0], longxrange[1]))

for scene in seq_dobjs:
    for obj in scene:
        if obj.y <= 222:
            if shortxrange[0] < obj.x and shortxrange[1] > obj.x :
                pos_x.append(obj.x)
                pos_y.append(obj.y)
        if obj.y <= 674 and obj.y > 222:
            if middlexrange[0] < obj.x and middlexrange[1] > obj.x :
                pos_x.append(obj.x)
                pos_y.append(obj.y)
        if obj.y > 674:
            if longxrange[0] < obj.x and longxrange[1] > obj.x:
                pos_x.append(obj.x)
                pos_y.append(obj.y)

print(short[2])
print(middle[2])
print(long[2])

plt.plot(pos_x, pos_y, 'ro')
plt.axis([-200,100 , 0, 1200])
plt.show()

"""
for i in range(0, len(seq_dobjs)-1):
    lastList = seq_dobjs[i]
    curList = seq_dobjs[i+1]

    for curObj in curList:
        minSim = 100
        matchObj = curObj
        for lastObj in lastList:
            tSim = curObj.Similarity(lastObj)
            if minSim > tSim:
                minSim = tSim
                matchObj = lastObj
        if minSim > 3.0:
            matchObj = curObj
            minSim = 1000

        if minSim < 3.0:
            print('match')
            curObj.print()
            matchObj.print()
            print(minSim)
    print('new scene')


#fp.close()
#print(numlines)
print(len(seq_dobjs))
"""




