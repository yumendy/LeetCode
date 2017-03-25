class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        else:
            while n % 3 == 0:
                n /= 3
            if n == 1 or n == 0:
                return True
            return False
