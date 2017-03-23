class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            index = abs(num) - 1
            nums[index] *= (-1 if nums[index] > 0 else 1)
        return [i + 1 for i in xrange(len(nums)) if nums[i] > 0]
