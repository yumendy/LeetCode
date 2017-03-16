class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        index = 0
        for num in nums:
            if (target - num) in dic:
                return [dic[(target - num)], index]
            dic[num] = index
            index += 1
