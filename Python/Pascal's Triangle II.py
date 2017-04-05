class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            return self.next_row(self.getRow(rowIndex - 1))
        
    def next_row(self, row):
        res = [row[i] + row[i - 1] for i in xrange(1, len(row))]
        res.insert(0, 1)
        res.append(1)
        return res
