class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is []:
            return 0
        else:
            for idx, num in enumerate(nums):
                if target <= num:
                    return idx
            else:
                return len(nums)
