class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        m, res = (n / 2, 2) if n % 2 == 0 else (n / 2 + 1, 1)
        for x in xrange(1, m):
            y = n - 2 * x
            res += self.fact(x + y) / (self.fact(x) * self.fact(y))
        return res
        
        
    def fact(self, n):
        res = 1
        for num in xrange(2, n + 1):
            res *= num
        return res
