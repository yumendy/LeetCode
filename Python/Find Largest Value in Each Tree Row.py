# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        else:
            queue = [(root, 0)]
            ans_list = []
            max_value = float('-inf')
            now_level = 0
            while len(queue) > 0:
                node, level = queue.pop(0)
                if level > now_level:
                    now_level = level
                    ans_list.append(max_value)
                    max_value = node.val
                else:
                    max_value = node.val if node.val > max_value else max_value
                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))
            ans_list.append(max_value)
            return ans_list
