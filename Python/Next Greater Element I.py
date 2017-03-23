class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        self.nums = nums
        return map(self.next_num_in_nums, findNums)
        
    def next_num_in_nums(self, num):
        try:
            index = self.nums.index(num) + 1
            for n in self.nums[index:]:
                if n > num:
                    return n
            else:
                return -1
        except:
            return -1