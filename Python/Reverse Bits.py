class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        s = bin(n)[2:]
        length_s = len(s)
        s = '0' * (32 - length_s) + s
        return int(s[::-1], 2)