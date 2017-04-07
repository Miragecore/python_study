from DetectedObject import *
from ReadData import ReadData
import matplotlib.pyplot as plt
from DirectoryFiles import *

#path = r"F:\garbage\1537"
path = r"F:\garbage\2017-03-23"  #RSU-08
#path = r"F:\garbage\RSU-14_170329"
lognames = GetDirectoryfileLists(path)

pos_x = []
pos_y = []
dist = []

#long-middle 674
#middle-shot 222

seq_dobjs = []
fileCount = 0
for logfilename in lognames:
    print(logfilename)
    tmp_seq = ReadData(path + "\\" + logfilename)
    seq_dobjs.append(tmp_seq)
    fileCount += 1
    if fileCount >= 1:
        break

print("processing")
#seq_dobjs = ReadData(logname)
sceneCount = 0
scene_x = []
scene_y = []
scene_dist = []
for minlog in seq_dobjs:  #분당 로그, 로그파일 1개씩
    for scene in minlog:
        #print(len(scene))
        for obj in scene:
            scene_x.append(obj.x)
            scene_y.append(obj.y)
            scene_dist.append(obj.distance)
        pos_x.append(scene_x[:])
        pos_y.append(scene_y[:])
        dist.append(scene_dist[:])
        sceneCount += 1
        scene_x.clear()
        scene_y.clear()
        scene_dist.clear()
"""
plt.scatter(pos_x[0], pos_y[0], marker='.')
print(len(pos_x[0]))
plt.scatter(pos_x[1], pos_y[1], marker='v')
print(len(pos_x[1]))
plt.scatter(pos_x[2], pos_y[2], marker='^')
print(len(pos_x[2]))
plt.scatter(pos_x[3], pos_y[3], marker='<')
print(len(pos_x[3]))
plt.scatter(pos_x[4], pos_y[4], marker='>')
print(len(pos_x[4]))
"""
indx = 10
plt.scatter([10] * len(dist[indx]), dist[indx], marker='.')
indx += 1
plt.scatter([11] * len(dist[indx]), dist[indx], marker='.')
indx += 1
plt.scatter([12] * len(dist[indx]), dist[indx], marker='.')
indx += 1
plt.scatter([13] * len(dist[indx]), dist[indx], marker='.')
indx += 1
plt.scatter([14] * len(dist[indx]), dist[indx], marker='.')
#for idx in range(10):
#    plt.scatter(pos_x[idx], pos_y[idx],marker='.')
    #plt.plot(pos_x[idx], pos_y[idx] , color=(idx*0.1, idx*0.1, idx*0.1, 1), marker='.')
    #plt.plot(pos_x[idx], pos_y[idx], color="red", marker='.')
#plt.plot(pos_x, pos_y, 'ro')
plt.show()






