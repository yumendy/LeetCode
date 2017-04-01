class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        result = num
        while result ** 2 > num:
            result = (result + num / result) / 2
        return result ** 2 == num