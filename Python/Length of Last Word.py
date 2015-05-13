class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        s = s.strip()
        l = len(s)
        if l is 0:
            return 0
        else:
            return l - 1 - s.rfind(" ")
