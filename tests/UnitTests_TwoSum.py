import Two_Sum
import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
       self.solution = Two_Sum.Solution()
    
    def test_twosum_found(self): 
        nums = [2, 7, 11, 15]
        target = 9
        result = self.solution.twoSum(nums, target)
        print(f"Testing twoSum ={nums} and target={target}")
        print(f"Result: {result}")
        self.assertEqual(result, [0, 1], "The indices should be [0, 1]")

    def test_twosum_no_solution(self): 
        nums = [1, 2, 3, 4]
        target = 10
        result = self.solution.twoSum(nums, target)
        print(f"Testing twoSum ={nums} and target={target}")
        print(f"Result: {result}")
        self.assertIsNone(result, "There is no valid pair")

    def test_twosum_empty(self): 
        nums = []
        target = 5
        result = self.solution.twoSum(nums, target)
        print(f"Testing twoSum with nums={nums} and target={target}")
        print(f"Result: {result}")
        self.assertIsNone(result, "There is no valid pair")

if __name__ == '__main__':
    unittest.main()


