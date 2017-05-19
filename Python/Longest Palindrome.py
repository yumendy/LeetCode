class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = collections.Counter(s)
        size = odd_flag = 0
        for num in dic.values():
            if num % 2 == 0:
                size += num
            else:
                size += num - 1
                odd_flag = 1
        return size + odd_flag
