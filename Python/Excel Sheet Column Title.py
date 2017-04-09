class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        import string
        map_dict = dict(zip(range(26), list(string.ascii_uppercase)))
        res = []
        while n > 0:
            res.append(map_dict[(n - 1) % 26])
            n = (n - 1) / 26
        return ''.join(res)[::-1]
