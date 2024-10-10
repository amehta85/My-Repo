import unittest
import Valid_Palindrome


class TestSolution(unittest.TestCase):
    
    def setUp(self):
        self.solution = Valid_Palindrome.Solution()
    
    def test_valid_palindromes(self):
        test_cases = ["A man, a plan, a canal, Panama","race car","12321"]  # valid palindromes
        for case in test_cases:
            result = self.solution.isPalindrome(case)
            print(f"Testing valid palindrome: '{case}' -> Result: {result}")
            self.assertTrue(result)
    
    def test_invalid_palindromes(self):
        test_cases = ["hello","12345"] # invalid palindromes
        for case in test_cases:
            result = self.solution.isPalindrome(case)
            print(f"Testing invalid palindrome: '{case}' -> Result: {result}")
            self.assertFalse(result)
    
    def test_emptystring(self):
        case = "" # empty string
        result = self.solution.isPalindrome(case)
        print(f"Testing empty string: '{case}' -> Result: {result}")
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
