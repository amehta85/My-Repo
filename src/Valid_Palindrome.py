class Solution(object):
    def isPalindrome(self, s):
        # Convert string to lowercase
        s = s.lower()
        # Join alphanumeric characters
        s = "".join(e for e in s if e.isalnum())
        # Check if the string is equal to its reverse
        return s == s[::-1]
