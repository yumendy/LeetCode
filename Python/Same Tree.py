class Solution:
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {boolean}
    def isSameTree(self, p, q):
        if (p is None) and (q is None):
            return True
        elif (p is None) or (q is None):
            return False
        else:
            if (p.val == q.val) and (self.isSameTree(p.left,q.left) and (self.isSameTree(p.right, q.right))):
                return True
            else:
                return False
