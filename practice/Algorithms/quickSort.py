import random

def quick_sort(my_array):
	quick_sort_helper(my_array, 0, len(my_array)-1)

def quick_sort_helper(my_array, first, last):
	if first < last:
		pivot = partition(my_array, first, last)

		quick_sort_helper(my_array, first, pivot - 1)
		quick_sort_helper(my_array, pivot + 1, last)

def partition(my_array, first, last):
	pivot_value = my_array[first]

	left_mark = first + 1
	right_mark = last

	done = False
	while not done:
		while left_mark <= right_mark and my_array[left_mark] <= pivot_value:
			left_mark += 1

		while right_mark >= left_mark and my_array[right_mark] >= pivot_value:
			right_mark -= 1

		if right_mark < left_mark:
			done = True
		else:
			swap_em(my_array, left_mark, right_mark)
	swap_em(my_array, first, right_mark)
	
	return right_mark

def swap_em(my_array, left_mark, right_mark):
	temp = my_array[left_mark]
	my_array[left_mark] = my_array[right_mark]
	my_array[right_mark] = temp


my_array = [int(100 * random.random()) for _ in range(20)]
print my_array
quick_sort(my_array)
print my_array
