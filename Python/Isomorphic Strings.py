class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        dic_value = {}
        
        for j, i in zip(s, t):
            if i in dic:
                if dic[i] != j:
                    return False
            else:
                dic[i] = j
                if j in dic_value:
                    return False
                dic_value[j] = i
        return True
