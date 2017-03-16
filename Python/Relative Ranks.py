class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        lst = sorted(nums, reverse=True)
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [str(num) for num in range(4, len(nums) + 1)]
        bind_dict = dict(zip(lst, rank))
        return [bind_dict[i] for i in nums]
