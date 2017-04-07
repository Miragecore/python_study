import math as math


class DetectedObject:
    def __init__(self, distance=0, angle=0, speed=0,
                 size=0, snr=0):
        self.size = size
        self.distance = distance
        self.angle = angle / 1000.0
        self.snr = snr
        self.speed = speed

        self.x = 0.0
        self.y = 0.0
        self.sx = 0.0
        self.sy = 0.0

        self.px = 0
        self.py = 0
        self.date = ""

        self.transform2xy()

    def transform2xy(self):
        self.factorx = math.sin(math.pi / 180 * self.angle)
        self.factory = math.cos(math.pi / 180 * self.angle)
        self.x = self.factorx * self.distance
        self.y = self.factory * self.distance
        self.sx = self.factorx * self.speed
        self.sy = self.factory * self.speed
        minY = self.distance - math.sin(math.pi/180 * 20)
        maxY = self.distance
        self.estimateY = (minY + maxY)/2

    def GetDistance(self, _y):
        return math.fabs(self.estimateY - _y)

    def Similarity(self, _dobj):
        speed_diff = math.fabs(self.speed - _dobj.speed)
        distance_diff = self.GetDistance(_dobj.estimateY)
        return speed_diff * 0.9 + distance_diff * 0.1

    def update(self, distance, angle, speed, size, snr):
        self.size = size
        self.distance = distance
        self.angle = angle
        self.snr = snr
        self.speed = speed

        self.transform2xy()

    def predict(self):
        self.px = self.x + self.sx /36
        #self.py = self.y + self.sy /36
        self.py = self.y + self.speed / 36


    def print(self):
        print(r"Size :{0}, Distance: {1}, Angle: {2}, "
              r"SNR: {3}, Speed: {4}".format(self.size,
                                               self.distance,
                                               self.angle,
                                               self.snr,
                                               self.speed))

    def printxy(self):
        print(r"size: {0}, x: {1}, y: {2}, "
              r"sx: {3}, sy: {4}".format(self.size,
                                         self.x,
                                         self.y,
                                         self.sx,
                                         self.sy))


