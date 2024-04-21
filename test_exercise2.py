import unittest
from Exercise2_find_the_largest_number import largest_number



class TestFindTheLargestNumber(unittest.TestCase):
    
    def test_find_largest_number(self):
        # Test finding the largest number among positive numbers
        self.assertEqual(largest_number([1, 2, 3, 4, 5, 6]), 6)
          
    def test_find_largest_negative_numbers(self):
        # Test finding the largest number among negative numbers
        self.assertEqual(largest_number([-1, -2, -3]), -1)

    def test_find_largest_zero_numbers(self):
        # Test finding the largest number among zeros
        self.assertEqual(largest_number([0, 0, 0]), 0)