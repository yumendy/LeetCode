# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = [(root, 1)]
        result_list = []
        for node, level in queue:
            if node:
                if len(result_list) < level:
                    result_list.insert(0, [])
                result_list[-level].append(node.val)
                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))
                
        
        return result_list
                
            
        