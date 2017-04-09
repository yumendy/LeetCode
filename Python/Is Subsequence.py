class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        len_s = len(s)
        i = 0
        for ch in t:
            if ch == s[i]:
                i += 1
                if i == len_s:
                    return True
        return False
