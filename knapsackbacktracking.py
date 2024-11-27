def knapsack_backtrack(weights, values, W, n):
    def knapsack_helper(i, current_weight, current_value):
        if i == n:
            return current_value
        max_value = knapsack_helper(i + 1, current_weight, current_value)
        if current_weight + weights[i] <= W:
            max_value = max(max_value, knapsack_helper(i + 1, current_weight + weights[i], current_value + values[i]))

        return max_value

    return knapsack_helper(0, 0, 0)

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
W = 5
n = len(weights)
print(f"Maximum value (backtracking): {knapsack_backtrack(weights, values, W, n)}")
