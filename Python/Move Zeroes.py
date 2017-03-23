class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_index = 0
        for i in xrange(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero_index] = nums[zero_index], nums[i]
                zero_index += 1
        