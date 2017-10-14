def isUnique(myString):
	myDirectory = set()
	for currentChar in myString:
		if currentChar not in myDirectory:
			myDirectory.add(currentChar)
		else:
			return False
	return True



myString = "abcd"
print myString + " is " + str(isUnique(myString))
myString2 = "abccd"
print myString2 + " is " + str(isUnique(myString2))