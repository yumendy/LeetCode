class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = min(nums)
        array_sum = 0
        for num in nums:
            if array_sum > 0:
                array_sum += num
            else:
                array_sum = num
            if array_sum > max_sum:
                max_sum = array_sum
        return max_sum