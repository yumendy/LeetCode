class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for index, num in enumerate(numbers):
            if target - num in dic:
                return [dic[target - num], index + 1]
            else:
                dic[num] = index + 1
            