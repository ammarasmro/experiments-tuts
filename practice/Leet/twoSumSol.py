# def twoSum(nums, target):

#     mySet = set()
#     i = 0
#     while i < len(nums)-1:
#     	if nums[i] not in mySet:
# 		    mySet.add(target-nums[i])
# 		    i += 1
# 		else:
# 			return [nums.index(i),i]


# print twoSum([2,7], 9)


def twoSum(nums, target):
	mySet = set()
	i = 0
	while i <= len(nums)-1:
		if nums[i] not in mySet:
			mySet.add(target-nums[i])
			i += 1
		else:
			return [nums.index(target-nums[i]),i]

print twoSum([1,2,3], 4)
print twoSum([2,7,9, 11], 9)

