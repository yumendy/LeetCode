class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = []
        num1 = num1[::-1]
        num2 = num2[::-1]
        if len(num1) < len(num2):
            num2, num1 = num1, num2
        c = 0
        i = 0
        while i < len(num1) and i < len(num2):
            k = int(num1[i]) + int(num2[i]) + c
            result.append(k % 10)
            c = k / 10
            i += 1
        while i < len(num1):
            k = int(num1[i]) + c
            result.append(k % 10)
            c = k / 10
            i += 1
        if c:
            result.append(c)
        result = map(str, result)
        return ''.join(result)[::-1]
