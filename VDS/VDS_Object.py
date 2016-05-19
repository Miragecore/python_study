class DetectObject:
	def __init__(self,time,oid, x, y, sx, sy, size):
		self.seqNo = 0
		self.time = time
		self.oid = oid
		self.x = x
		self.y = y
		self.sx = sx
		self.sy = sy
		self.size = size
		self.eventType = 0

class TrackingObject:
	def __init__(self, oid, x, y, sx, sy, size):
		self.oid = oid
		self.x = x
		self.y = y
		self.sx = sx
		self.sy = sy
		self.size = size
		self.lostcount = 0
		self.IsCounted = False
		self.bUpdated = False

	def __init__(self, dObj):
		self.oid = dObj.oid
		self.x = dObj.x
		self.y = dObj.y
		self.sx = dObj.sx
		self.sy = dObj.sy
		self.size = dObj.size
		self.lostcount = 0
		self.IsCounted = False
		self.bUpdated = False
		



