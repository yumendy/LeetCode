class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        s = int("",join(map(str, digits))) + 1
        result = []
        while s > 0:
            result.append(s % 10)
            s /= 10
        result.reverse()
        return result