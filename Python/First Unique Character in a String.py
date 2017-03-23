class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for ch in s:
            if ch in dic:
                dic[ch] += 1
            else:
                dic[ch] = 1
        for index, ch in enumerate(s):
            if dic[ch] == 1:
                return index
        else:
            return -1
            