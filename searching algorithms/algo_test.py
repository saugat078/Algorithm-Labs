import unittest
from linear_search import linear_search
from binary_search import binary_search

class LinearBinarySearchTest(unittest.TestCase):
    def test_linear_search(self):
        arr = [2, 5, 7, 8, 10, 12]
        self.assertEqual(linear_search(arr, 7),2)
        self.assertEqual(linear_search(arr, 8),3)
        self.assertEqual(linear_search(arr, 12),5)
        self.assertEqual(linear_search(arr, 6),-1)
    
    def test_binary_search(self):
        arr = [2, 5, 7, 8, 10, 12]
        self.assertEqual(binary_search(arr, 7),2)
        self.assertEqual(binary_search(arr, 8),3)
        self.assertEqual(binary_search(arr, 12),5)
        self.assertEqual(binary_search(arr, 6),-1)
    

if __name__=="__main__":
    unittest.main()
