class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        index = 0
        ns = ''
        while index < len(s):
            ns += s[index:index+k][::-1] + s[index + k:index + 2 * k]
            index += 2*k
        return ns