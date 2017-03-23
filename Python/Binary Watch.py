class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        l = []
        for i in xrange(12):
            for j in xrange(60):
                if bin(i).count('1') + bin(j).count('1') == num:
                    l.append('%d:%02d' % (i,j))
        return l
        