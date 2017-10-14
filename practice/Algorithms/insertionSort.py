import random
my_array = [int(10 * random.random()) for _ in range(10)]
print my_array

def insertion_sort(my_array):
	for j in range(1,len(my_array)):
		key = my_array[j]
		i = j - 1
		while i >= 0 and my_array[i] > key:
			my_array[i+1] = my_array[i]
			i -= 1
		my_array[i + 1] = key

insertion_sort(my_array)

print my_array