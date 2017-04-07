from DetectedObject import *
from ReadData import ReadData
import matplotlib.pyplot as plt
from DirectoryFiles import *

import re


pos_x = []
pos_y = []
short = [0.0, 0, 0.0 , 0.0] #Sum, Count Avg stdev
middle = [0.0, 0, 0.0, 0.0]
long = [0.0, 0, 0.0, 0.0]
#long-middle 674
#middle-shot 222

seq_dobjs = []

seq_dobjs = ReadData(r"F:\itsk 성능평가 준비\RSU-08\보행자오검\log.11.13.txt")
print("processing")

with open("Anal.txt", "w", encoding="UTF8") as fp:
    for scene in seq_dobjs:
        for obj in scene:
            if math.fabs(obj.speed) < 7:
                fp.writelines("{0},{1},{2},{3},{4}\n".format(obj.date, obj.x, obj.y, obj.speed,obj.size))




