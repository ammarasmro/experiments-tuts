def compressThis(myString):
	cacheChar = ''
	charCounter = 0
	storage = []
	
	for currentChar in myString:
		if len(storage) == 0 or currentChar is not cacheChar:
			cacheChar = currentChar
			storage.append(cacheChar)
			storage.append(1)
		elif currentChar == cacheChar:
			storage[len(storage)-1] += 1

	if len(storage) > len(myString):
		return myString
	return ''.join(map(str,storage))



myString = "aabcccccaaa"
print compressThis(myString)