class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dic = {}
        dic_value = {}
        
        word_list = str.split()
        if len(pattern) != len(word_list):
            return False
        
        for i, j in zip(pattern, word_list):
            if i in dic:
                if dic[i] != j:
                    return False
            else:
                if j in dic_value:
                    return False
                else:
                    dic[i] = j
                    dic_value[j] = i
        return True
        