class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums == []:
            return []
        res = [1]
        for idx, num in enumerate(nums[:-1]):
            res.append(res[idx] * num)
        pi_num = 1
        idx = len(nums) - 1
        while idx >= 0:
            res[idx] *= pi_num
            pi_num *= nums[idx]
            idx -= 1
        return res