class Solution(object):
    def longestPalindrome(self, s):
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
        odd_flag = 0
        size = 0
        for key in dic:
            if dic[key] % 2 == 0:
                size += dic[key]
            else:
                odd_flag = 1
                if dic[key] > 1:
                    size += dic[key] - 1
        return size + odd_flag