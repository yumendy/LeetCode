class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i = 0
        counter = 0
        
        for c in g:
            for i in xrange(i, len(s)):
                if s[i] >= c:
                    counter += 1
                    i += 1
                    break
        return counter
