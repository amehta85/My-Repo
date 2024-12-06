# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(t1, t2):
            if not t1 and not t2:  # Both are None, symmetric
                return True
            if not t1 or not t2:  # One of them is None, not symmetric
                return False
            # Check if current nodes are equal and their subtrees are mirror images
            return (t1.val == t2.val) and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

        # An empty tree is symmetric
        if not root:
            return True
        
        # Check if the left and right subtrees of the root are mirrors of each other
        return isMirror(root.left, root.right)
