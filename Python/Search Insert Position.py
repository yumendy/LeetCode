class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        if len(nums) == 0 or nums[0] >= target:
            return 0
        elif len(nums) == 1:
            return 1
        else:
            for x in xrange(1,len(nums)):
                if target > nums[x - 1] and target <= nums[x]:
                    return x
            return len(nums)