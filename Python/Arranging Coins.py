class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = 1
        res = 0
        while res <= n:
            res += k
            k += 1
        return k - 2