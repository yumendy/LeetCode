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
    def preorderTraversal(self, root):
        self.result = []
        if root is not None:
            self.result.append(root.val)
            if root.left is not None:
                self.Traverse(root.left)
            if root.right is not None:
                self.Traverse(root.right)
        return self.result

    def Traverse(self, node):
        self.result.append(node.val)
        if node.left is not None:
            self.Traverse(node.left)
        if node.right is not None:
            self.Traverse(node.right)
