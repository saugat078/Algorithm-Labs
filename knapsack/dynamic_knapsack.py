def knapsack_dp(W, wt, val, n):
    # table to store the maximum value that can be obtained for each subproblem
    # The table has n+1 rows (for 0 to n items) and W+1 columns (for 0 to W weight)
    table = [[0 for j in range(W+1)] for i in range(n+1)]

    # table items filled in bottom-up manner
    for i in range(1, n+1):
        for j in range(1, W+1):
            if wt[i-1] > j:
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = max(val[i-1] + table[i-1][j-wt[i-1]], table[i-1][j])

    return table[n][W]


# val = [280,100,120,120]
# wt = [40,10,20,24]
# W = 60
# n = len(wt)
# max_value = knapsack_dp(W, wt, val, n)

# print("Maximum value:", max_value)