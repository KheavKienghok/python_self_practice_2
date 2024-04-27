import unittest
from Exercise9_find_common_element import find_common_num

class TestFindCommonNum(unittest.TestCase):
    
    def test_find_commn(self):
        # Test case with one common number
        self.assertEqual(find_common_num([1, 2, 3, 4], [2, 5, 6, 7]), [2])

        # Test case with no common numbers
        self.assertEqual(find_common_num([1, 2, 3, 4], [5, 6, 7]), [])

        # Test case with all common numbers
        self.assertEqual(find_common_num([1, 2, 3, 4], [1, 2, 3, 4]), [1, 2, 3, 4])

        # Test case with empty lists
        self.assertEqual(find_common_num([], []), [])

        # Test case with one empty list
        self.assertEqual(find_common_num([1, 2, 3, 4], []), [])

        # Test case with negative numbers
        self.assertEqual(find_common_num([-1, -2, -3, -4], [-2, -5, -6, -7]), [-2])

        # Test case with duplicate numbers
        self.assertEqual(find_common_num([1, 2, 2, 3, 4], [2, 2, 5, 6, 7]), [2])