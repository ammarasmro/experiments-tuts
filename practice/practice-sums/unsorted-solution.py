def hasPairWithSum(lst, intendedSum):
	complementSet = set()
	found = False
	for currentValue in lst:
		if currentValue not in complementSet:
			complementSet.add(intendedSum - currentValue)
		else:
			found = True
			break
	return found

lst = [1, 2, 3, 9]
intendedSum = 8
print lst
print hasPairWithSum(lst, intendedSum)

lst = [1, 2, 4, 4]
intendedSum = 8
print lst
print hasPairWithSum(lst, intendedSum)