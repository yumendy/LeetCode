class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        self.map_dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        self.res = list(self.map_dic[digits[0]])
        map(self.string_mul, digits[1:])
        return self.res

    def string_mul(self, s2):
        self.res = ['%s%s' % (sub_s1, sub_s2) for sub_s1 in self.res for sub_s2 in self.map_dic[s2]]
