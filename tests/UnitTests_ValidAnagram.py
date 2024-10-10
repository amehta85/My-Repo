import unittest
import valid_anagram
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = valid_anagram.Solution()

    def test_anagram(self):
        # Test cases where strings are anagrams
        self.assertTrue(self.solution.isAnagram("listen", "silent"))
        self.assertTrue(self.solution.isAnagram("anagram", "nagaram"))
        self.assertTrue(self.solution.isAnagram("rat", "tar"))

    def test_not_anagram(self):
        # Test cases where strings are not anagrams
        self.assertFalse(self.solution.isAnagram("hello", "world"))
        self.assertFalse(self.solution.isAnagram("rat", "car"))

    def test_empty_strings(self):
        # Test case where both strings are empty
        self.assertTrue(self.solution.isAnagram("", ""))