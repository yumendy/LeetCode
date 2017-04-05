class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1] * (i) for i in xrange(1,numRows + 1)]
        for i in xrange(2, numRows):
            for j in xrange(1, len(res[i]) - 1):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res
        