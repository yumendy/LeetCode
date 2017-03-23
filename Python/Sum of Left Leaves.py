# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = 0
        self.find(root)
        return self.sum
        
    def is_leaf(self, node):
        return node.left == None and node.right == None
    
    def find(self, root):
        if root is None:
            return
        if root.left != None and self.is_leaf(root.left):
            self.sum += root.left.val
        else:
            self.find(root.left)
        self.find(root.right)