import random

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2  
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1  


random_array = [random.randint(1, 1000) for _ in range(10)]
target_value = random.choice(random_array)  
random_array.sort() 

print(f"The random array: {random_array}")
print(f"The target value: {target_value}")

result = binary_search(random_array, target_value)

if result != -1:
    print(f"Target {target_value} found at index {result}.")
else:
    print(f"Target {target_value} not found.")
