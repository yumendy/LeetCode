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
    def postorderTraversal(self, root):
        self.result = []
        self.Traversal(root)
        return self.result

    def Traversal(self,node):
        if node != None:
            self.Traversal(node.left)
            self.Traversal(node.right)
            self.result.append(node.val)
