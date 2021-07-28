# Selection Sort
# Implement the selection sort algorithm that is sorting in descending order.

def selection_sort_desc(arr):
    for i in range(0, len(arr)):
        max_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr

print(selection_sort_desc([5,34,5,4646,242,2425252,2324,1]))