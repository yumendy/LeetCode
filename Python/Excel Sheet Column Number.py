class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum(map(lambda a: (a[1] - 64) * pow(26, a[0]), list(enumerate(map(ord, s)[::-1]))))
