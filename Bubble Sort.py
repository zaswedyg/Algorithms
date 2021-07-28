# Bubble Sort
# Implement the bubble sort algorithm that is sorting in descending order.

def bubble_sort_desc(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
    return arr
print(bubble_sort_desc([3,5,42,443,4,2424,]))