arr = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]


# Linear search to find the number 9
# Linear search is a good choice for an unsorted list because
# it does not require the list to be sorted in order to work.
# Linear search simply compares the target value to each element in the list until it finds a match.
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


linear_result = linear_search(arr, 9)
print(f'Linear Search: Number 9 {"found" if linear_result != -1 else "not found"} at index {linear_result}')


# Sort the array using Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


insertion_sort(arr)
print('Array after Insertion Sort:', arr)


# Binary search on the sorted array to find the number 9
# Binary Search is very efficient when searching for elements in a large,
# sorted dataset, such as in phone books, dictionaries, or database indexing.
# If you had a large sorted dataset of products,
# you could use Binary Search to quickly locate a product by its identifier.
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


binary_result = binary_search(arr, 9)
print(f'Binary Search: Number 9 {"found" if binary_result != -1 else "not found"} at index {binary_result}')
