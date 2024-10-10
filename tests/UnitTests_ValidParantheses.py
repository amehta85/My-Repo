import unittest
import Valid_Parantheses
class TestIsValid(unittest.TestCase):

    def setUp(self):
        self.solution = Valid_Parantheses.Solution()

    def test_valid_parentheses(self):
        # Test cases where the string of brackets is valid
        self.assertTrue(self.solution.isValid("()"))
        self.assertTrue(self.solution.isValid("()[]{}"))
        self.assertTrue(self.solution.isValid("{[()]}"))

    def test_invalid_parentheses(self):
        # Test cases where the string of brackets is invalid
        self.assertFalse(self.solution.isValid("(]"))
        self.assertFalse(self.solution.isValid("([)]"))
        self.assertFalse(self.solution.isValid("{[}"))

    def test_empty_string(self):
        # An empty string is considered valid as there are no unbalanced brackets
        self.assertTrue(self.solution.isValid(""))