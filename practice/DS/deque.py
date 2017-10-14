class Deque():
	def __init__(self):
		self.items=[]

	def addFront(self, item):
		self.items.append(item)

	def addRear(self, item):
		self.items.insert(0,item)

	def popFront(self):
		return self.items.pop()

	def popRear(self):
		return self.pop(0)

	def size(self):
		return len(items)

	def isEmpty(self):
		return len(self.items) == 0


d = Deque()
print d.isEmpty()