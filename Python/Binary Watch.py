class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        l = []
        for i in xrange(12):
            for j in xrange(60):
                if self.count_bit(i) + self.count_bit(j) == num:
                    l.append('%d:%02d' % (i, j))
        return l

    def count_bit(self, num):
        num = (num & 0x55) + ((num >> 1) & 0x55)
        num = (num & 0x33) + ((num >> 2) & 0x33)
        num = (num & 0x0f) + ((num >> 4) & 0x0f)
        return num
