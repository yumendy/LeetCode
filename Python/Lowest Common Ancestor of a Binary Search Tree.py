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
        self.pre_travel_list = []
        self.pre_order(root)
        p_path = self.find_path(p)
        q_path = self.find_path(q)
        pre_node = root
        for i, j in zip(p_path, q_path):
            if i != j:
                return pre_node
            else:
                pre_node = i
        else:
            return pre_node
        
    def find_path(self, node):
        path_to_node = [node]
        index = self.pre_travel_list.index(node)
        current_node = node
        index -= 1
        while index >=0:
            if self.pre_travel_list[index].left == current_node:
                current_node = self.pre_travel_list[index]
                path_to_node.insert(0, current_node)
            elif self.pre_travel_list[index].right == current_node:
                current_node = self.pre_travel_list[index]
                path_to_node.insert(0, current_node)
            index -= 1
        return path_to_node
    
    def pre_order(self, root):
        if root:
            self.pre_travel_list.append(root)
            self.pre_order(root.left)
            self.pre_order(root.right)
        