class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        temp = 0
        while num > 0:
            temp += num % 10
            num /= 10
        if temp < 10:
            return temp
        else:
            return self.addDigits(temp)
