class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = 1
        counter = 0
        while counter < n:
            counter += 9 * k * 10 ** (k - 1)
            k += 1
        k -= 1
        counter -= 9 * k * 10 ** (k - 1)
        remain = n - counter
        nth = remain % k
        num_num = remain / k
        if nth == 0:
            return (10 ** (k - 1) + num_num - 1) % 10
        else:
            return int(str(10 ** (k - 1) + num_num)[nth - 1])
