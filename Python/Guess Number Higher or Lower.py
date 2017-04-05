# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 1
        b = n
        try_num = (a + b) / 2
        ret = guess(try_num)
        while ret != 0:
            if ret == 1:
                if a == try_num:
                    a += 1
                else:
                    a = try_num
            else:
                b = try_num
            try_num = (a + b) / 2
            ret = guess(try_num)
        return try_num