def toDict(myStrToDict):
	myDict = {}
	for currentChar in myStrToDict:
		if currentChar not in myDict:
			myDict[currentChar] = 0
		myDict[currentChar] += 1
	return myDict


def isPerm(myString1, myString2):
	Dict1 = toDict(myString1)
	Dict2 = toDict(myString2)
	for currentChar in Dict2.keys():
		if currentChar not in Dict1.keys():
			return False
		elif Dict1[currentChar] != Dict2[currentChar]:
			return False
	return True

myString1 = "abcd"
myString2 = "badc"
print myString1 + " and " + myString2 + " are permutations: " + str(isPerm(myString1, myString2))

myString1 = "abcd"
myString2 = "bafc"
print myString1 + " and " + myString2 + " are permutations: " + str(isPerm(myString1, myString2))