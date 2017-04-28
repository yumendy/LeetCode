# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.pre_order = []
        self.pre_travel(root)
        for idx in xrange(len(self.pre_order) - 1):
            self.pre_order[idx].right = self.pre_order[idx + 1]
            self.pre_order[idx].left = None
        self.pre_order[-1].right = None
        root = self.pre_order[0]
    
    def pre_travel(self, root):
        if not root:
            return None
        else:
            self.pre_order.append(root)
            self.pre_travel(root.left)
            self.pre_travel(root.right)
