def greedy_knapsack(weights, values, capacity):
    n = len(weights)

    ratios = [(values[i] / weights[i], i) for i in range(n)]
    ratios.sort(reverse=True, key=lambda x: x[0])

    total_value = 0
    total_weight = 0
    selected_items = []

    for ratio, i in ratios:
        if total_weight + weights[i] <= capacity:
            total_value += values[i]
            total_weight += weights[i]
            selected_items.append(i + 1)  

    return total_value, total_weight, selected_items


weights = [4, 2, 6, 3, 5]
values = [12, 1, 10, 7, 6]
capacity = 20

total_value, total_weight, selected_items = greedy_knapsack(weights, values, capacity)

print(f"Total value: {total_value}")
print(f"Total weight: {total_weight}")
print(f"Selected items: {selected_items}")
