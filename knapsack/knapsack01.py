def knapsack_brute_force_01(W, wt, val, n):

    max_value = 0

    for i in range(2**n):
        bin_str = bin(i)[2:].zfill(n)
        total_weight = 0
        total_value = 0
        for j in range(n):
            if bin_str[j] == '1':
                total_weight += wt[j]
                total_value += val[j]
        if total_weight <= W and total_value > max_value:
            max_value = total_value

    return max_value

# val = [280,100,120,120]
# wt = [40,10,20,24]
# W = 60
# n = len(wt)
# max_value = knapsack_brute_force_01(W, wt, val, n)

# print("Maximum value:", max_value)