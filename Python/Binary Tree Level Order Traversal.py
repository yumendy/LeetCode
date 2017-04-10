# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [(root, 0)]
        res = []
        temp = []
        level = 0
        while len(queue) > 0:
            node, l = queue.pop(0)
            if l == level:
                temp.append(node.val)
            else:
                res.append(temp)
                temp = [node.val]
                level = l
            if node.left:
                queue.append((node.left, l + 1))
            if node.right:
                queue.append((node.right, l + 1))
        res.append(temp)
        return res
