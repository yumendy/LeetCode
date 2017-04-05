# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.path_stack = []
        self.res = []
        self.travel(root)
        return self.res
    
    def travel(self, root):
        if root is None:
            return
        self.path_stack.append(str(root.val))
        if self.is_leaf(root):
            self.res.append('->'.join(self.path_stack))
        else:
            if root.left:
                self.travel(root.left)
                self.path_stack.pop()
            if root.right:
                self.travel(root.right)
                self.path_stack.pop()
            
    def is_leaf(self, root):
        return root.left == root.right
        