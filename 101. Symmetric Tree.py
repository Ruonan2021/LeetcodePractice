# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        else:
            return self.isSymmetricHelper(root.left, root.right)
        
        
    def isSymmetricHelper(self, left, right):
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        elif left.val == right.val:
                outFlag = self.isSymmetricHelper(left.left, right.right)
                innerFlag = self.isSymmetricHelper(left.right, right.left)
                return outFlag and innerFlag  # Here only use and, can't use ==, since False == False return True while it shoud be False
        else:
            return False
        
        # This problems creates a helpher function, which is similar to 100.Same tree         