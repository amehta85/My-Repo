class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        if p is None and q is None:  # Both trees are empty
            return True
        
        if p is None or q is None: # One tree is empty, and the other is not
            return False
        
        if p.val != q.val: # value of current nodes are different
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) # always checking the left and right subtrees



        