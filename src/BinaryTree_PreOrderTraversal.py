# Definition for a binary tree node.
from typing import List, Optional
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            result.append(node.val)  # Visit the node
            if node.right:
                stack.append(node.right)  # Push right child to stack
            if node.left:
                stack.append(node.left)   # Push left child to stack

        return result