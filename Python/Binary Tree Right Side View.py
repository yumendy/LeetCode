# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        queue = [(root, 0)]
        res = []
        temp = []
        now_level = 0
        while len(queue) > 0:
            node, level = queue.pop(0)
            if level == now_level:
                temp.append(node.val)
            else:
                res.append(temp)
                temp = [node.val]
                now_level = level
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        res.append(temp)
        return [item[-1] for item in res if item != []]
