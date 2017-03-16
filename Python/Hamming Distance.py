class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        result = 0
        temp = x ^ y
        while temp > 0:
            result += temp - ((temp >> 1) << 1)
            temp >>= 1
        return result
