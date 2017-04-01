class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels_list = list(filter(lambda ch: ch in 'aeiouAEIOU', s))
        s = list(s)
        for i, ch in enumerate(s):
            if ch in 'aeiouAEIOU':
                s[i] = vowels_list.pop()
        return ''.join(s)
