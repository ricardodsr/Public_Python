# Function to determine if a `target` exists in the sorted list `nums`
# or not using a binary search algorithm
def binarySearch(nums, target):

	# search space is nums[left…right]
	(left, right) = (0, len(nums) - 1)

	# loop till the search space is exhausted
	while left <= right:

		# find the mid-value in the search space and
		# compares it with the target

		mid = (left + right) // 2

		# overflow can happen. Use:
		# mid = left + (right - left) / 2
		# mid = right - (right - left) // 2

		# target is found
		if target == nums[mid]:
			return mid

		# discard all elements in the right search space,
		# including the middle element
		elif target < nums[mid]:
			right = mid - 1

		# discard all elements in the left search space,
		# including the middle element
		else:
			left = mid + 1

	# `target` doesn't exist in the list
	return -1


if __name__ == '__main__':

	nums = [2, 5, 6, 8, 9, 10]
	target = 5

	index = binarySearch(nums, target)

	if index != -1:
		print('Element found at index', index)
	else:
		print('Element found not in the list')


# Recursive implementation of the binary search algorithm to return
# the position of `target` in subarray nums[left…right]
def binarySearch(nums, left, right, target):

	# Base condition (search space is exhausted)
	if left > right:
		return -1

	# find the mid-value in the search space and
	# compares it with the target

	mid = (left + right) // 2

	# overflow can happen. Use below
	# mid = left + (right - left) / 2

	# Base condition (a target is found)
	if target == nums[mid]:
		return mid

	# discard all elements in the right search space,
	# including the middle element
	elif target < nums[mid]:
		return binarySearch(nums, left, mid - 1, target)

	# discard all elements in the left search space,
	# including the middle element
	else:
		return binarySearch(nums, mid + 1, right, target)


if __name__ == '__main__':

	nums = [2, 5, 6, 8, 9, 10]
	target = 5

	(left, right) = (0, len(nums) - 1)
	index = binarySearch(nums, left, right, target)

	if index != -1:
		print('Element found at index', index)
	else:
		print('Element found not in the list')
