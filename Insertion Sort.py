# Insertion Sort
# Implement the insertion sort algorithm that is sorting in descending order.

def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(insertion_sort_desc([1,23,43,53,12,313,0]))