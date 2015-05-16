class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        l = len(s) - 1
        Sum = 0
        for c in s:
            Sum += (ord(c) - 64) * 26 ** l
            l -= 1
        return Sum
