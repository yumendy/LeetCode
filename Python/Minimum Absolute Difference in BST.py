# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.min_diff = self.prev = 2 **32 - 1
        self.get_min(root)
        return self.min_diff
        
        
    def get_min(self, tree):
        if tree:
            self.get_min(tree.left)
            self.min_diff = min(self.min_diff, abs(self.prev - tree.val))
            self.prev = tree.val
            self.get_min(tree.right)
    