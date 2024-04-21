import unittest
from Exercise7_find_prime_number import find_prime_number


class TestFindPrimeNumber(unittest.TestCase):
    
    # Test finding prime numbers within a given range
    def test_find_prime(self):
        self.assertEqual(find_prime_number(list(range(0, 99))), [
                                                                2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                                                                31, 37, 41, 43, 47, 53, 59, 61, 67,
                                                                71, 73, 79, 83, 89, 97
                                                                ])
    
    # Test with a smaller range of numbers
    def test_find_prime_small_range(self):
        self.assertEqual(find_prime_number(list(range(0, 10))), [2, 3, 5, 7])
    
    # Test with a range of numbers where there are no prime numbers
    def test_find_prime_no_primes(self):
        self.assertEqual(find_prime_number(list(range(0, 11, 2))), [2])
    
    # Test with a single number
    def test_find_prime_single_number(self):
        self.assertEqual(find_prime_number([7]),[7])
        
        
    # Test with negative numbers
    def test_find_prime_negative_numbers(self):
        self.assertEqual(find_prime_number(list(range(-10, 0))), [])
    
    # Test with zero
    def test_find_prime_zero(self):
        self.assertEqual(find_prime_number([0]), [])
    
    # Test with None input
    def test_find_prime_none_input(self):
        self.assertEqual(find_prime_number([]), [])