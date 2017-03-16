class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        nums.sort()
        for i in nums:
            if i != index:
                return index
            index += 1
        return index
