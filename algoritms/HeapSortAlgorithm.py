#HeapSortAlgorithm
#In-place Heapsort Implementation

# return left child of `A[i]`
def LEFT(i):
	return 2*i + 1


# return right child of `A[i]`
def RIGHT(i):
	return 2*i + 2


# Utility function to swap two indices in a list
def swap(A, i, j):

	temp = A[i]
	A[i] = A[j]
	A[j] = temp


# Recursive heapify-down algorithm. The node at index `i` and
# its two direct children violates the heap property
def heapify(A, i, size):

	# get left and right child of node at index `i`
	left = LEFT(i)
	right = RIGHT(i)

	largest = i

	# compare `A[i]` with its left and right child
	# and find the largest value
	if left < size and A[left] > A[i]:
		largest = left

	if right < size and A[right] > A[largest]:
		largest = right

	# swap with a child having greater value and
	# call heapify-down on the child
	if largest != i:
		swap(A, i, largest)
		heapify(A, largest, size)


# Function to remove an element with the highest priority (present at the root)
def pop(A, size):

	# if the heap has no elements
	if size <= 0:
		return -1

	top = A[0]

	# replace the root of the heap with the last element
	# of the list
	A[0] = A[size - 1]

	# call heapify-down on the root node
	heapify(A, 0, size - 1)

	return top


# Function to perform heapsort on a list `A` of size `n`
def heapsort(A):

	# build a priority queue and initialize it by the given list
	n = len(A)

	# Build-heap: Call heapify starting from the last internal
	# node all the way up to the root node
	i = (n - 2) // 2
	while i >= 0:
		heapify(A, i, n)
		i = i - 1

	# repeatedly pop from the heap till it becomes empty
	while n:
		A[n - 1] = pop(A, n)
		n = n - 1


if __name__ == '__main__':

	A = [6, 4, 7, 1, 9, -2]

	# perform heapsort on the list
	heapsort(A)

	# print the sorted list
	print(A)



