class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        dic = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000}
        for index, ch in enumerate(s[:-1]):
            if dic[ch] < dic[s[index + 1]]:
                count -= dic[ch]
            else:
                count += dic[ch]
        return count + dic[s[-1]]
        
        