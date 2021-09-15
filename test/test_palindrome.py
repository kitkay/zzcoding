#Import unit test built-in function
import unittest

#Import file to be test.
from palindromeChecker import Palindrome

class TestStringPalindrome(unittest.TestCase):

    # Make a static string to test and call sanitize method as global
    stringToCheck = "!@#$%^amazinGnizam.<>?()_a"
    sanitizedString = Palindrome.sanitizeData(stringToCheck)

    #Checking if the global sanitization succeeded.
    def test_sanitizeData(self):
        try:
            self.assertTrue(self.sanitizedString)
            pass
            print("Sanitize Data Passed!")
        except:
            print("Sanitize Data Failed!")

    #Match sanitized data to indicated string
    def test_sanitizeMatch(self):
        try:
            self.assertEqual(self.sanitizedString, 'amazingnizama')
            pass
            print("Sanitize \""+self.stringToCheck+"\" to "+self.sanitizedString+" Passed!")
        except:
            print('Sanitized data did not match indicated string')

    # Check if the sanitized data is a palindrome or not
    def test_isPalindrome(self):
        # palCheck = self.getString.isPalindrome()
        palCheck = Palindrome.isPalindrome(self.sanitizedString)
        try:
            self.assertTrue(palCheck)
            pass
            print("Palindrome string passed!")
        except:
            print("Palindrome string failed!")

    # def test_checkPalindrome(self

if __name__ == '__main__':
    unittest.main()