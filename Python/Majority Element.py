class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        l = len(nums) / 2
        dic = {}
        for item in nums:
            if item in dic:
                dic[item] += 1
                if dic[item] > l:
                    return item
            else:
                dic[item] = 1
        for item in dic:
        	if dic[item] > l:
        		return item