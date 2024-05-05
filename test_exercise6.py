import unittest
from Exercise6_check_palindrome import check_palindrome

class TestCheckPalidrio(unittest.TestCase):
    
    # Test for a palindrome word
    def test_check_palindrome_palindrome(self):
        self.assertTrue(check_palindrome("lol"))

    # Test for a non-palindrome word
    def test_check_palindrome_non_palindrome(self):
        self.assertFalse(check_palindrome("hello"))

    # Test for an empty string
    def test_check_palindrome_empty_string(self):
        self.assertTrue(check_palindrome(""))

    # Test for a single character (should always be a palindrome)
    def test_check_palindrome_single_character(self):
        self.assertTrue(check_palindrome("a"))

    # Test for case-insensitive palindrome
    def test_check_palindrome_case_insensitive(self):
        self.assertTrue(check_palindrome("Racecar"))
        self.assertTrue(check_palindrome("rAcEcAr"))
        self.assertTrue(check_palindrome("A man a plan a canal Panama"))

    # Test for palindromes with whitespace and punctuation
    def test_check_palindrome_whitespace_and_punctuation(self):
        self.assertTrue(check_palindrome("A man, a plan, a canal, Panama!"))
        self.assertTrue(check_palindrome("Was it a car or a cat I saw?"))
        self.assertTrue(check_palindrome("Never odd or even."))

    # Test for a long palindrome word
    def test_check_palindrome_long_word(self):
        self.assertTrue(check_palindrome("deified"))
        
    # Test for invalid input (not a string)
    def test_check_palindrome_invalid_input(self):
        with self.assertRaises(TypeError):
            check_palindrome(123)
            check_palindrome(3.14)
            check_palindrome(['a', 'b', 'c'])
            
            
        