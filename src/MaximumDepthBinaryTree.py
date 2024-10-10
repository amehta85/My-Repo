# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        #:type root: TreeNode
        #:rtype: int
        if root is None:  # tree is empty, the depth is 0
            return 0
        
        left_depth = self.maxDepth(root.left)  # depth of the left subtree
        right_depth = self.maxDepth(root.right)  # depth of the right subtree
        
        return max(left_depth, right_depth) + 1  # depth of node is the maximum depth of subtrees plus 1
