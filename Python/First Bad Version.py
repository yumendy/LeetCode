# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 and isBadVersion(1):
            return 1
            
        low = 1
        high = n
        while low < high:
            mid = (low + high) / 2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid
            if low == high - 1 and not isBadVersion(low) and isBadVersion(high):
                return high
        return low
