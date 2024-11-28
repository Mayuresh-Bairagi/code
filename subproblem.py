def find_subsets(arr, target):
    def backtrack(index, current_subset, current_sum):
        if current_sum == target:
            subsets.append(current_subset[:])
            return
        
        if current_sum > target or index == len(arr):
            return
        
        current_subset.append(arr[index])
        backtrack(index + 1, current_subset, current_sum + arr[index])

        current_subset.pop()
        backtrack(index + 1, current_subset, current_sum)
    
    subsets = []
    backtrack(0, [], 0)
    return subsets

arr = [3, 34, 4, 12, 5, 2]
target = 9
subsets = find_subsets(arr, target)

print(f"The array is {arr}")
if subsets:
    print(f"Subsets that sum to {target}:")
    for subset in subsets:
        print(subset)
else:
    print(f"No subsets found that sum to {target}")



"""Time  Complexity
Recursive Backtracking : O(n.2^n)
Dynamic Programming (DP) : O(n*target)
"""
