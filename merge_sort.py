def merge_sort(items):
    """
    Sorts a list of strings by string length using the Merge Sort algorithm.

    Args:
    - items (list): The list of strings to be sorted.

    Returns:
    list: The sorted list of strings.
    """
    n = len(items)
    temporary_storage = [None] * n
    size_of_subsections = 1

    while size_of_subsections < n:
        for i in range(0, n, size_of_subsections * 2):
            i1_start, i1_end = i, min(i + size_of_subsections, n)
            i2_start, i2_end = i1_end, min(i1_end + size_of_subsections, n)
            sections = (i1_start, i1_end), (i2_start, i2_end)
            merge(items, sections, temporary_storage)

        size_of_subsections *= 2

    return items


def merge(items, sections, temporary_storage):
    """
    Merges two subsections of a list based on the length of strings.

    Args:
    - items (list): The list containing string elements.
    - sections (tuple): A tuple of two sections to be merged.
    - temporary_storage (list): Temporary storage for merging.

    Returns:
    None: The merged subsections are stored in the original list.
    """
    (start_1, end_1), (start_2, end_2) = sections
    i_1 = start_1
    i_2 = start_2
    i_t = 0

    while i_1 < end_1 or i_2 < end_2:
        if i_1 < end_1 and i_2 < end_2:
            if len(items[i_1]) > len(items[i_2]):
                temporary_storage[i_t] = items[i_1]
                i_1 += 1
            else:
                temporary_storage[i_t] = items[i_2]
                i_2 += 1
        elif i_1 < end_1:
            temporary_storage[i_t] = items[i_1]
            i_1 += 1
        else:  # i_2 < end_2
            temporary_storage[i_t] = items[i_2]
            i_2 += 1

        i_t += 1

    for i in range(start_1, end_2):
        items[i] = temporary_storage[i - start_1]


# Lists
list1 = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "indigo", "jackfruit"]
list2 = ["kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine"]
list3 = ["watermelon", "xylophone", "yellow", "zebra", "apricot", "blueberry", "coconut", "dragonfruit", "eggplant", "fennel"]

# Sort the lists by string length
sorted_list1 = merge_sort(list1)
sorted_list2 = merge_sort(list2)
sorted_list3 = merge_sort(list3)

# Print the sorted lists
print("Sorted List 1 (by string length):", sorted_list1)
print("Sorted List 2 (by string length):", sorted_list2)
print("Sorted List 3 (by string length):", sorted_list3)
