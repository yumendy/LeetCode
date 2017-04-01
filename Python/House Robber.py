class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        elif nums == []:
            return 0
        else:
            money = [nums[0], max(nums[0], nums[1])]
            for index in xrange(2, len(nums)):
                money.append( max(money[index - 2] + nums[index], money[index - 1]))
            return money[-1]
                