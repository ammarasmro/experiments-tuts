def hasPairWithSum(lst, intendedSum):
	low = 0
	high = len(lst) - 1
	found = False
	
	while not found and low < high:
		currentSum = lst[low] + lst[high]
		if currentSum > intendedSum:
			high -= 1
		elif currentSum < intendedSum:
			low += 1
		else:
			found = True

	return found

lst = [1, 2, 3, 9]
findSum = 8
print lst
print hasPairWithSum(lst, findSum)

lst = [1, 2, 4, 4]
findSum = 8
print lst
print hasPairWithSum(lst, findSum)
