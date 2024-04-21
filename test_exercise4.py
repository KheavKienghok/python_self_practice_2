import unittest
from Exercise4_calculate_sum_of_2d_list import sum_2d_list

class TestCalcilateSum(unittest.TestCase):
    
    def test_calculate_sum_single_row(self):
        # Test summing up a single row
        self.assertEqual(sum_2d_list([[1, 2, 3, 4, 5, 6, 7]]), 28)
    
    def test_calculate_sum_multiple_rows(self):
        # Test summing up multiple rows
        self.assertEqual(sum_2d_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 45)
    
    def test_calculate_sum_empty_list(self):
        # Test summing up an empty list
        self.assertEqual(sum_2d_list([]), 0)
    
    def test_calculate_sum_single_column(self):
        # Test summing up a single column
        self.assertEqual(sum_2d_list([[1], [2], [3], [4], [5]]), 15)
    
    def test_calculate_sum_negative_numbers(self):
        # Test summing up a list containing negative numbers
        self.assertEqual(sum_2d_list([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]), -45)
    
    def test_calculate_sum_mixed_numbers(self):
        # Test summing up a list containing positive, negative, and zero numbers
        self.assertEqual(sum_2d_list([[1, -2, 3], [4, 0, -6], [-7, 8, -9]]), -8)
