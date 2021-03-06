class Queue():
	def __init__(self):
		self.items = []

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		return self.items.pop()

	def isEmpty(self):
		return len(self.items) == 0

	def size(self):
		return len(self.items)



q = Queue()
print q.size()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print q.dequeue()
print q.dequeue()
print q.size()