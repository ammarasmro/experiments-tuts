class BinaryTree:
	def __init__(self, value):
		self.value = value
		self.leftChild = None
		self.rightChild = None

	def insertLeft(self, item):
		if self.leftChild == None:
			self.leftChild = BinaryTree(item)
		else:
			temp = BinaryTree(item)
			temp.leftChild = self.leftChild
			self.leftChild = temp

	def insertRight(self, item):
		if self.rightChild == None:
			self.rightChild = BinaryTree(item)
		else:
			temp = BinaryTree(item)
			temp.leftChild = self.leftChild
			self.leftChild = temp

	def getLeftChild(self):
		return self.leftChild

	def getRightChild(self):
		return self.rightChild

	def getRootVal(self):
		return self.value

	def setRootVal(self, item):
		self.value = item

r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())
