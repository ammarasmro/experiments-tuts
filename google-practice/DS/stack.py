class Stack():
	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peak(self):
		return self.items[-1]

	def isEmpty(self):
		return len(self.items) == 0

	def size(self):
		return len(self.items)

	def getStack(self):
		return self.items

s = Stack()
print s.getStack()
s.push(1)
s.push(2)
s.pop()
s.peak()
s.push(3)
print s.getStack()
print s.size()