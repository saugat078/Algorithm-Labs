import unittest
from insertion_sort import insertion_sort
from merge_sort import merge_sort

class testalgo(unittest.TestCase):
    def test_insertion_sort(self):
        arr=[10,20,18,16,25,30]
        self.assertEqual(insertion_sort(arr),[10, 16, 18, 20, 25, 30])

        arr2 = [10, 20, 30, 40, 50]
        self.assertEqual(insertion_sort(arr2), [10, 20, 30, 40, 50])

        arr3 = [50, 40, 30, 20, 10]
        self.assertEqual(insertion_sort(arr3), [10, 20, 30, 40, 50])

        arr4 = []
        self.assertEqual(insertion_sort(arr4), [])
        
        
    def test_merge_sort(self):
         arr1 = [10,20,18,16,25,30]
         self.assertEqual(merge_sort(arr1), [10, 16, 18, 20, 25, 30])

         arr2 = [10, 20, 30, 40, 50]
         self.assertEqual(merge_sort(arr2), [10, 20, 30, 40, 50])

         arr3 = [50, 40, 30, 20, 10]
         self.assertEqual(merge_sort(arr3), [10, 20, 30, 40, 50])

         arr4 = []
         self.assertEqual(merge_sort(arr4), [])
        
    
if __name__=="__main__":
    unittest.main()