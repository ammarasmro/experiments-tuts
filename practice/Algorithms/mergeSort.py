import random
def merge_sort(A, p, r):
	if p < r:
		q = (p + r)/2
		merge_sort(A,p,q)
		merge_sort(A,q+1,r)
		merge(A,p,q,r)

def merge(A,p,q,r):
	left = A[p:q+1]
	right = A[q+1:r+1]
	i, j, k = 0, 0, p
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			A[k] = left[i]
			i += 1
		else:
			A[k] = right[j]
			j += 1
		k += 1
	while i < len(left):
		A[k] = left[i]
		i += 1
		k += 1
	while j < len(right):
		A[k] = right[j]
		j += 1
		k += 1

my_array = [int(50 * random.random()) for _ in range(20)]
print my_array
merge_sort(my_array, 0, len(my_array))
print my_array