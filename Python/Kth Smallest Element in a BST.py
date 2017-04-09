# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.ans = None
        self.counter = 0
        self.travel(root)
        return self.ans
    
    def travel(self, root):
        if not root:
            return
        else:
            if not self.ans:
                self.travel(root.left)
            self.counter += 1
            if self.counter == self.k:
                self.ans = root.val
            if not self.ans:
                self.travel(root.right)
