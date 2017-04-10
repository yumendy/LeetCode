# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.res = []
        self.find_path(root, p)
        path_to_p = self.res[::-1]
        self.res = []
        self.find_path(root, q)
        path_to_q = self.res[::-1]
        for item in zip(path_to_p, path_to_q):
            if item[0] == item[1]:
                last = item[0]
            else:
                break
        return last
    
    def find_path(self, root, node):
        if not root:
            return False
        if root is node:
            self.res.append(root)
            return True
        else:
            if self.find_path(root.left, node) or self.find_path(root.right, node):
                self.res.append(root)
                return True
            else:
                return False
