# Import and allow regex to be used
import re
"""
    Palindrome checker for any string.
"""
class Palindrome:

    # Sanitize data.
    def sanitizeData(data):
        # convert to lower string then remove all puntuations and special chars.
        lowerData = data.lower()
        sanitized = re.sub(r'[^\w]|(\_)', '', lowerData)
        return sanitized

    # Palindrome checker.
    def isPalindrome(data):
        # Check if sanitized string matches its reversed value.
        return (True if data == data[::-1] else False)


#Data input for palindrome checking.
inputData = "!@#$%^amazinGnizama.<>?()_"

# Test an input for palindrome.
sanitize = Palindrome.sanitizeData(inputData)
# print(Palindrome.isPalindrome(sanitize))