class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n % 2 == 0:
            m = n / 2
            res = 2
            for x in xrange(1, m):
                y = n - 2 * x
                res += self.fact(x + y) / (self.fact(x) * self.fact(y))
            return res
        else:
            m = n / 2
            res = 1
            for x in xrange(1, m + 1):
                y = n - 2 * x
                res += self.fact(x + y) / (self.fact(x) * self.fact(y))
            return res
        
        
        
    def fact(self, n):
        res = 1
        for num in xrange(2, n + 1):
            res *= num
        return res