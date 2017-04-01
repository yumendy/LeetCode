class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        else:
            while num % 4 == 0:
                num /= 4
            if num == 1:
                return True
            else:
                return False
        