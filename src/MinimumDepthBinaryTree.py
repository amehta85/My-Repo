from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        # Initialize a queue for BFS with the root node and its depth (1)
        queue = deque([(root, 1)])  # Each element is a tuple (node, depth)
        
        while queue:
            node, depth = queue.popleft()
            
            # If we reach a leaf node, return the current depth
            if not node.left and not node.right:
                return depth
            
            # Otherwise, add the child nodes to the queue with an incremented depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
