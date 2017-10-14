def binarySearch(my_array, item):
	if len(my_array) == 0: 
		return False
	else:
		mid = len(my_array) / 2
		if my_array[mid] == item:
			return True
		else:
			if my_array[mid] > item:
				return binarySearch(my_array[:mid], item)
			else:
				return binarySearch(my_array[mid+1:], item)
	






my_array = [x for x in range(1,40,3)]
print my_array
print binarySearch(my_array, 18)