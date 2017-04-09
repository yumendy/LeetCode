class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        length_h = len(haystack)
        length_n = len(needle)
        if not needle:
            return 0
        if length_n > length_h or not haystack or not needle:
            return -1
        else:
            for start in xrange(length_h - length_n + 1):
                if haystack[start:start + length_n] == needle:
                    return start
            return -1
