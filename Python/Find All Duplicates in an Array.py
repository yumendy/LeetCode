class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                ans.append(abs(num))
            else:
                nums[idx] *= -1
        return ans
