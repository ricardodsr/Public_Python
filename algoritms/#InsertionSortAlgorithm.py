#InsertionSortAlgorithm interactive

# Function to perform insertion sort on a list
def insertionSort(A):
 
    # Start from the second element
    # (the element at index 0 is already sorted)
    for i in range(1, len(A)):
 
        value = A[i]
        j = i
 
        # find index `j` within the sorted subset `A[0…i-1]`
        # where element `A[i]` belongs
        while j > 0 and A[j - 1] > value:
            A[j] = A[j - 1]
            j = j - 1
 
        # Note that sublist `A[j…i-1]`is shifted to
        # the right by one position, i.e., `A[j+1…i]`
 
        A[j] = value
 
 
if __name__ == '__main__':
 
    A = [3, 8, 5, 4, 1, 9, -2]
 
    insertionSort(A)
 
    # print the sorted list
    print(A)

# Recursive function to perform insertion sort on sublist `A[i…n]`
def insertionSort(A, i, n):
 
    value = A[i]
    j = i
 
    # find index `j` within the sorted subset `A[0…i-1]`
    # where element `A[i]` belongs
    while j > 0 and A[j - 1] > value:
        A[j] = A[j - 1]
        j = j - 1
 
    A[j] = value
 
    # Note that sublist `A[j…i-1]`is shifted to
    # the right by one position, i.e., `A[j+1…i]`
 
    if i + 1 <= n:
        insertionSort(A, i + 1, n)
 
 
if __name__ == '__main__':
 
    A = [3, 8, 5, 4, 1, 9, -2]
 
    # start from the second element (the element at index 0 is already sorted)
    insertionSort(A, 1, len(A) - 1)
 
    # print the sorted list
    print(A)
