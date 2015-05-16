# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    result = []
    def inorderTraversal(self, root):
        self.result = []
        if root is not None:
            self.Traver(root)
        return self.result
    def Traver(self, node):
        if node.left is not None:
            self.Traver(node.left)
        self.result.append(node.val)
        if node.right is not None:
            self.Traver(node.right)