# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        else:
            self.s = 0
            self.travel(root)
            return root
    
    def travel(self, root):
        if not root:
            return
        else:
            self.travel(root.right)
            self.s, root.val = self.s + root.val, self.s + root.val
            self.travel(root.left)
