def quick_sort(arr):
    if len(arr) <= 1:
        return arr  
    pivot = arr[len(arr) - 1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

unsorted_array = [38, 27, 43, 3, 9, 82, 10]
sorted_array = quick_sort(unsorted_array)

print("Unsorted Array:", unsorted_array)
print("Sorted Array:", sorted_array)
