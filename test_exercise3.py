import unittest
from Exercise3_reverse_string import reverse_string

class TestReverseString(unittest.TestCase):
    
    def test_reverse_string(self):
        # Test a simple string
        self.assertEqual(reverse_string("Hello"), "olleH")
        
    
    def test_empty_string(self):    
        # Test an empty string
        self.assertEqual(reverse_string(""), "")
        
        # Test a string with spaces
        self.assertEqual(reverse_string("   "), "   ")
        
    def test_special_reverse_string(self):
        # Test a string with special characters
        self.assertEqual(reverse_string("!@#$"), "$#@!")
        
        
    def test_reverse_number(self):
        # Test a string with numbers
        self.assertEqual(reverse_string("12345"), "54321")
        
        
        
