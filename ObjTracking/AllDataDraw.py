from DetectedObject import *
from ReadData import ReadData
import matplotlib.pyplot as plt
from DirectoryFiles import *

import re

#logname = "log.09.36.txt"
#logname = "log.15.40.txt"  #RSU08
#logname = "KumgangBr.txt"

#path = r"F:\garbage\1537"
#path = r"F:\garbage\2017-03-23"  #RSU-08
path = r"F:\garbage\RSU-68-170330" #rsu-68
#path = r"F:\garbage\RSU-14_170329"
lognames = GetDirectoryfileLists(path)

pos_x = []
pos_y = []
short = [0.0, 0, 0.0 , 0.0] #Sum, Count Avg stdev
middle = [0.0, 0, 0.0, 0.0]
long = [0.0, 0, 0.0, 0.0]
#long-middle 674
#middle-shot 222
seq_dobjs = []
for logfilename in lognames:
    print(logfilename)
    tmp_seq = ReadData(path + "\\" + logfilename)
    seq_dobjs.append(tmp_seq)

print("processing")
#seq_dobjs = ReadData(logname)
for minlog in seq_dobjs:
    for scene in minlog:
        print(len(scene))
        for obj in scene:
            if math.fabs(obj.speed) < 7:
                pos_x.append(obj.x)
                pos_y.append(obj.y)

#plt.plot(pos_x, pos_y, 'ro')

#RSU-08
plt.hist2d(pos_y, pos_x, [500, 100], range=[[0, 1000], [-5, 5]])
plt.axis([0, 1000, -5, 5])
#RSU-14
#plt.hist2d(pos_x, pos_y, [150, 500])
#plt.axis([-10, 65, 0, 1000])

plt.show()





