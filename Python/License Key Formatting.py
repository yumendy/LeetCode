class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s_without_dish = S.replace('-', '').upper()
        length = len(s_without_dish)
        if length < K:
            return s_without_dish
        first = length % K
        if first != 0:
            res = s_without_dish[:first] + '-'
        else:
            res = ''
        return res + '-'.join([(s_without_dish[(first + K * i): (first + K * i + K)]) for i in xrange((length - first) / K)])
