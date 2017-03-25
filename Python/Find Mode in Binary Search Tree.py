# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        dic = {}
        if not root:
            return []
        queue = [root]
        while len(queue) > 0:
            node = queue.pop(0)
            if node.val in dic:
                dic[node.val] += 1
            else:
                dic[node.val] = 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        l = [i for i in dic.iteritems()]
        l.sort(key = lambda x: x[1], reverse = True)
        return map(lambda x: x[0], filter(lambda x: x[1] == l[0][1], l))