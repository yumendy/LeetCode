# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        self.deepth(root)
        return self.result
        
        
        
    def deepth(self, root):
        if root == None:
            return 0
        else:
            left_deepth = self.deepth(root.left)
            right_deepth = self.deepth(root.right)
            self.result = max(self.result, left_deepth + right_deepth)
            return max(left_deepth, right_deepth) + 1