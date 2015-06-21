class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        if x < 0:
        	x = int(str(x)[:0:-1]) * -1
        else:
        	x = int(str(x)[::-1])
        if (x > 2 ** 31 -1) or x < (-1 * 2 ** 31):
        	return 0
        else:
        	return x