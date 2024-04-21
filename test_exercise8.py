import unittest
from Exercise8_fibonacci_sequence import fibonacci_sequence

class TestFibonacciSequence(unittest.TestCase):
    
    # Test Fibonacci sequence generation with valid input
    def test_fibonacci(self):
        self.assertEqual(fibonacci_sequence(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    # Test whether function returns [] for empty input
    def test_empty_input(self):
        self.assertEqual(fibonacci_sequence(0), [])

    # Test whether function returns "Invalid input!" for invalid input (negative integer)
    def test_invalid_input(self):
        self.assertEqual(fibonacci_sequence(-5), "Invalid input!")
