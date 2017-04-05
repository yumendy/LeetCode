# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        left_stack =[root.left]
        right_stack = [root.right]
        
        while left_stack != [] and right_stack != []:
            left = left_stack.pop(0)
            right = right_stack.pop(0)
            if left == None and right == None:
                pass
            elif left == None or right == None:
                return False
            elif left.val != right.val:
                return False
            if left and right:
                left_stack.append(left.left)
                left_stack.append(left.right)
                right_stack.append(right.right)
                right_stack.append(right.left)
        else:
            return True
                
    
    
        
        