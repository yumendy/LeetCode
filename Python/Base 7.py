class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        s = ''
        flag = '' if num >= 0 else '-'
        num = abs(num)
        if num == 0:
            return '0'
        while num > 0:
            s += str(num % 7)
            num /= 7
        return flag + s[::-1]
