class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = map(str, xrange(1, n + 1))
        res.sort()
        return map(int, res)
