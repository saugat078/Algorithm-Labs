def bruteforce_knapsack(W, wt, val, n):
    maxProfit = 0
    solutions = [format(x, '04b') for x in range(2**n)]
    print(solutions)
    for sol in solutions:
        a = []
        for i, x in enumerate(sol):
            if x == '0':
                a.append(i)
        print(a)
        profit = sum(int(sol[i])*val[i] for i in range(n))
        weight = sum(int(sol[i])*wt[i] for i in range(n))
        print(profit)
        print(weight)
        fraction = 0
        if weight < W:
            for i in a:
                if W-weight < wt[i]:
                    remaining = W - weight
                else:
                    remaining = wt[i]
                frac = (val[i] / wt[i]) * remaining
                if frac > fraction:
                    fraction = frac
        profit += fraction
        if weight <= W and profit >= maxProfit:
            maxProfit = profit
    return int(maxProfit)


val = [280,100,120,110]
# val = [60, 100, 120,120]
wt = [40,10,20,24]
# wt = [10, 20, 30,24]
W = 50
n = len(val)
print("Maximum value in fractional knapsack using Bruteforce method: ", bruteforce_knapsack(W, wt, val, n))