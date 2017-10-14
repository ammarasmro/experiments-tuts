def isPalindromePerm(myString):
	lowString = myString.lower()
	myDict = {}
	for currentChar in lowString:
		if currentChar not in myDict.keys():
			myDict[currentChar] = 0
			myDict[currentChar] += 1
		elif myDict[currentChar] == 1:
			myDict[currentChar] = 0
		else:
			myDict[currentChar] += 1

	counter = 0
	for i in myDict.keys():
		if i != " ":
			counter += myDict[i]
	if counter > 1:
		return False
	return True



myString = "Tact Coa"
print isPalindromePerm(myString)

myString = "Tact Coah"
print isPalindromePerm(myString)