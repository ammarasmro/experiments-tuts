def isOneEdit(myString1, myString2):
	if abs(len(myString1)-len(myString2)) > 1:
		return False
	counter = 0
	str1Iter = 0
	str2Iter = 0
	while str1Iter < len(myString1) - 1 and str2Iter < len(myString2) - 1:
		if myString1[str1Iter] != myString2[str2Iter]:
			counter += 1
			if myString1[str1Iter+1] == myString2[str2Iter]:
				str1Iter += 1
			elif myString1[str1Iter] == myString2[str2Iter]:
				str2Iter += 1
		str1Iter += 1
		str2Iter += 1
		if counter > 1:
			return False
	return True

myString1 = "pale"
myString2 = "ple"

print isOneEdit(myString1, myString2)

myString1 = "pales"
myString2 = "pale"

print isOneEdit(myString1, myString2)

myString1 = "pale"
myString2 = "bale"

print isOneEdit(myString1, myString2)

myString1 = "pale"
myString2 = "bake"

print isOneEdit(myString1, myString2)