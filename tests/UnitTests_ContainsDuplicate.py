import unittest
import ContainsDuplicate
class TestSolution(unittest.TestCase):
    
    def setUp(self):
        self.solution = ContainsDuplicate.Solution()

    def test_no_duplicates(self):
        nums = [1, 2, 3, 4]
        self.assertFalse(self.solution.containsDuplicate(nums), "no duplicates")

    def test_with_duplicates(self):
        nums = [1, 2, 3, 4, 1]
        self.assertTrue(self.solution.containsDuplicate(nums), "duplicates")

    def test_empty_list(self):
        nums = []
        self.assertFalse(self.solution.containsDuplicate(nums), "no duplicates - empty list")

    def test_negative_numbers(self):
        nums = [-1, -2, -3, -1]
        self.assertTrue(self.solution.containsDuplicate(nums), "duplicates with negative numbers")

if __name__ == '__main__':
    unittest.main()
