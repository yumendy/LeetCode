class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        re = nums[0]
        for num in nums[1:]:
            re ^= num
        return re