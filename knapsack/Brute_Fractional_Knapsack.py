def fractional_knapsack_brute_force(W, wt, val, n):
    # Generate all possible subsets
    subsets = []
    for i in range(2**n):
        subset = [int(x) for x in format(i, f'0{n}b')]
        subsets.append(subset)

    # Compute total value and weight of each subset
    total_values = []
    total_weights = []
    for subset in subsets:
        total_value = sum([v*w for v, w in zip(val, subset)])
        # print(total_value)
        total_weight = sum([w*s for w, s in zip(wt, subset)])
        total_values.append(total_value)
        total_weights.append(total_weight)

    # Compute maximum possible value for each subset
    max_values = []
    for i in range(len(subsets)):
        if total_weights[i] <= W:
            remaining_weight = W - total_weights[i]
            remaining_items = [j for j in range(n) if subsets[i][j] == 0]
            if remaining_items:
                max_val_per_weight = max([val[j]/wt[j] for j in remaining_items])
                max_val_item = max([val[j] for j in remaining_items if val[j]/wt[j] == max_val_per_weight])
                max_val_weight = wt[val.index(max_val_item)]
                max_val_fraction = min(1, remaining_weight/max_val_weight)
                max_value = total_values[i] + max_val_fraction*max_val_item
            else:
                max_value = total_values[i]
        else:
            max_value = 0
        max_values.append(max_value)
    return max(max_values)

# val = [280,100,120,120]
# wt = [40,10,20,24]
# W = 60
# n = len(val)
# print("Maximum value: ", fractional_knapsack_brute_force(W, wt, val, n))