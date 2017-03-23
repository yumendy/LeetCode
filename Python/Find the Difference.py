class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ls = list(s)
        lt = list(t)
        ls.sort()
        lt.sort()
        ls.append(None)
        for i , j in zip(ls, lt):
            if i != j:
                return j