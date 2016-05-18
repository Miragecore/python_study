
class disJointItem():
	def __init__(self,label):
		self.parent = self
		self.rank = 0
		self.label = label			

	def FindRoot(self):
		if self.parent != self :
			self.parent = self.parent.FindRoot()
		return self.parent
		'''
		if self.parent == self :
			return self
		else :
			return Find(self.parent)
		'''

	def Merge(self,y):
		xRoot = self.FindRoot()
		yRoot = y.FindRoot()

		if xRoot == yRoot :
			return

		if xRoot.rank < yRoot.rank :
			xRoot.parent = yRoot
		elif xRoot.rank > yRoot.rank :
			yRoot.parent = xRoot
		else :
			yRoot.parent = xRoot
			xRoot.rank = xRoot.rank + 1

class disjointForest():
  def __init__(self):
    self.items = {0:disJointItem(0)}

  def isDictItem(self, lbl):
    return lbl in self.items

  def AddItem(self, lbl):
    if self.isDictItem(lbl):
      return

    self.items[lbl] = disJointItem(lbl)

  def GetItem(self, lbl):
    if self.isDictItem(lbl):
      return self.items[lbl]

    return None

  def MergeByLabel(self, lbl1, lbl2):
    item1 = self.GetItem(lbl1)
    item2 = self.GetItem(lbl2)

    item1.Merge(item2)


