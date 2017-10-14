class BinaryHeap:
	def __init__(self):
		self.heap = [0]
		self.currentSize = 0

	def percUp(self, i):
		while i / 2 > 0:
			if self.heap[i] < self.heap[i/2]:
				temp = self.heap[i/2]
				self.heap[i/2] = self.heap[i]
				self.heap[i] = temp
			i = i / 2

	def insert(self, item):
		self.heap.append(item)
		self.currentSize += 1
		self.percUp(self.currentSize)

	def percDown(self, i):
		while i*2 <= self.currentSize:
			mc = self.minChild(i)
			if self.heap[i] > self.heap[mc]:
				temp = self.heap[i]
				self.heap[i] = self.heap[mc]
				self.heap[mc] = temp
			i = mc

	def minChild(self, i):
		if i*2+1 > self.currentSize:
			return i * 2
		else:
			if self.heap[i*2] < self.heap[i*2+1]:
				return i*2
			else:
				return i*2+1

	def delMin(self):
		retVal = self.heap[1]
		self.heap[1] = self.heap[self.currentSize]
		self.currentSize -= 1
		self.heap.pop()
		self.percDown(1)
		return retVal
		
	def size(self):
		return self.currentSize

	def isEmpty(self):
		return self.currentSize == 0

	def buildHeap(self, listToHeap):
		i = len(listToHeap) / 2
		self.currentSize = len(listToHeap)
		self.heap = [0] + listToHeap[:]
		while i > 0:
			self.percDown(i)
			i -= 1


bh = BinaryHeap()
bh.buildHeap([9,5,6,2,3])

print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
