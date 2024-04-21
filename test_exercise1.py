import unittest
from Exercise1_multipilcation_table import multiplication


class TestMultiple(unittest.TestCase):
    
    # Test multiplication table for positive numbers
    def test_multiplication(self):
        self.assertEqual(multiplication(3), "3  * 1  = 3\n3  * 2  = 6\n3  * 3  = 9\n3  * 4  = 12\n3  * 5  = 15\n3  * 6  = 18\n3  * 7  = 21\n3  * 8  = 24\n3  * 9  = 27\n3  * 10 = 30\n")
        self.assertEqual(multiplication(5), "5  * 1  = 5\n5  * 2  = 10\n5  * 3  = 15\n5  * 4  = 20\n5  * 5  = 25\n5  * 6  = 30\n5  * 7  = 35\n5  * 8  = 40\n5  * 9  = 45\n5  * 10 = 50\n")
        self.assertEqual(multiplication(7), "7  * 1  = 7\n7  * 2  = 14\n7  * 3  = 21\n7  * 4  = 28\n7  * 5  = 35\n7  * 6  = 42\n7  * 7  = 49\n7  * 8  = 56\n7  * 9  = 63\n7  * 10 = 70\n")
        self.assertEqual(multiplication(10), "10 * 1  = 10\n10 * 2  = 20\n10 * 3  = 30\n10 * 4  = 40\n10 * 5  = 50\n10 * 6  = 60\n10 * 7  = 70\n10 * 8  = 80\n10 * 9  = 90\n10 * 10 = 100\n")

    # Test multiplication table for negative numbers
    def test_negative_multiplication(self):
        self.assertEqual(multiplication(-5), "-5 * 1  = -5\n-5 * 2  = -10\n-5 * 3  = -15\n-5 * 4  = -20\n-5 * 5  = -25\n-5 * 6  = -30\n-5 * 7  = -35\n-5 * 8  = -40\n-5 * 9  = -45\n-5 * 10 = -50\n")
        self.assertEqual(multiplication(-2), "-2 * 1  = -2\n-2 * 2  = -4\n-2 * 3  = -6\n-2 * 4  = -8\n-2 * 5  = -10\n-2 * 6  = -12\n-2 * 7  = -14\n-2 * 8  = -16\n-2 * 9  = -18\n-2 * 10 = -20\n")
        self.assertEqual(multiplication(-9), "-9 * 1  = -9\n-9 * 2  = -18\n-9 * 3  = -27\n-9 * 4  = -36\n-9 * 5  = -45\n-9 * 6  = -54\n-9 * 7  = -63\n-9 * 8  = -72\n-9 * 9  = -81\n-9 * 10 = -90\n")

    # Test multiplication table for zero
    def test_zero_multiplication(self):
        self.assertEqual(multiplication(0), "0  * 1  = 0\n0  * 2  = 0\n0  * 3  = 0\n0  * 4  = 0\n0  * 5  = 0\n0  * 6  = 0\n0  * 7  = 0\n0  * 8  = 0\n0  * 9  = 0\n0  * 10 = 0\n")