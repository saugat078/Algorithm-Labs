def greedy_fractional_knapsack(W, wt, val):
    
    value_per_weight = [v/w for v, w in zip(val, wt)]

    sorted_items = sorted(zip(value_per_weight, wt, val), reverse=True)
    current_weight = 0
    current_value = 0

    for value_per_weight, weight, value in sorted_items:
        if current_weight + weight <= W:
            current_weight += weight
            current_value += value
        else:
            fraction = (W - current_weight) / weight
            current_weight += fraction * weight
            current_value += fraction * value
            break

    return current_value


# val = [280,100,120,120]
# wt = [40,10,20,24]
# W = 60

# max_value = greedy_fractional_knapsack(W, wt, val)

# print("Maximum value:", max_value)