def knapsack_dp(weights, values, W, n):
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    taken = [0] * n  
    w = W
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            taken[i - 1] = 1
            w -= weights[i - 1] 

    return dp[n][W], taken


weights = [2, 1, 4, 5]
values = [3, 4, 5, 6]
W = 5
n = len(weights)

max_value, taken = knapsack_dp(weights, values, W, n)
print(f"Maximum value: {max_value}")
print(f"Items taken (binary array): {taken}")
