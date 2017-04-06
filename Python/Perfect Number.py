class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        s = 0
        for i in xrange(2, int(num ** 0.5) + 1):
            if num % i == 0:
                s += i
                s += (num / i)
                if s > num:
                    return False
        
        return s + 1 == num
