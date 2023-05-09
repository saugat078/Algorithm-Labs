import unittest
from Brute_Fractional_Knapsack import fractional_knapsack_brute_force
from knapsack01 import knapsack_brute_force_01
from greedy_frac_knapsack import greedy_fractional_knapsack
from dynamic_knapsack import knapsack_dp

class Knapsack_test(unittest.TestCase):

    def test_bruteforce_fractional_knapsack(self):
        val = [280,100,120,120]
        wt = [40,10,20,24]
        W = 60
        n = len(val)
        output = 440
        input = fractional_knapsack_brute_force(W, wt, val, n)
        self.assertEqual(input, output)  

    def test_knapsack_01(self):
        wt = [10, 20, 30]
        val = [60, 100, 120]
        W = 50
        n = len(wt)
        output = 220
        input =knapsack_brute_force_01(W, wt, val, n)
        self.assertEqual(input, output)  

    def test_greedy_fractional_knapsack(self):
        wt = [10, 20, 30]
        val = [60, 100, 120]
        W = 50
        output = 240
        input = greedy_fractional_knapsack(W, wt,val)
        self.assertEqual(input, output)

    def test_dynamic_01_knapsack(self):
        val = [20,5,10,40,15,25]
        wt = [1,2,3,8,7,4]
        W = 10
        n = len(val)
        output = 60
        input = knapsack_dp(W, wt, val, n)
        self.assertEqual(input, output)
    

if __name__ == "__main__":
    unittest.main()