# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [(root, 0)]
        ans = None
        while len(queue) > 0:
            temp_node = queue.pop(0)
            node, level = temp_node
            if not ans:
                ans = temp_node
            else:
                if level > ans[1]:
                    ans = temp_node
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        return ans[0].val
