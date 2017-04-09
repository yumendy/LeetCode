class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        else:
            nums.sort()
            i = 0
            j = 1
            counter_list = []
            while i < len(nums) - 1:
                if nums[j] - nums[i] == k:
                    counter_list.append((nums[i], nums[j]))
                if j == len(nums) - 1 or nums[j] - nums[i] > k :
                    i += 1
                    j = i + 1
                else:
                    j += 1
            return len(set(counter_list))