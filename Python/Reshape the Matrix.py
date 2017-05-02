class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        temp = sum(nums, [])
        if r * c > len(temp):
            return nums
        else:
            return [temp[i * c:i * c + c] for i in xrange(r)]
