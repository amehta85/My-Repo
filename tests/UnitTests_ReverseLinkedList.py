import unittest 
import Reverse_LinkedList

class TestSolution(unittest.TestCase):
    def setUp(self):
       self.solution = Reverse_LinkedList.Solution()

def test_reverse_empty_list(self):
        head = self.list_to_linked_list([])
        reversed_head = self.solution.reverseList(head)
        self.assertEqual(self.linked_list_to_list(reversed_head), [])

def test_reverse_single_element_list(self):
        head = self.list_to_linked_list([1])
        reversed_head = self.solution.reverseList(head)
        self.assertEqual(self.linked_list_to_list(reversed_head), [1])

        if __name__ == '__main__':
            unittest.main()
