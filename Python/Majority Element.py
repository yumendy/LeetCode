class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = collections.Counter(nums)
        t = c.items()
        t.sort(key=lambda x: x[1], reverse=True)
        return t[0][0]
