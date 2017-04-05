class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        length = len(nums)
        if length == 1:
            return 1
        
        i =  0

        while i < length - 1:
            if nums[i + 1] != nums[i]:
                i += 1
            else:
                break
        else:
            return  i + 1
        
        i += 1
        j = i
        now_num = nums[i]
        while j < length:
            if nums[j] != now_num:
                nums[i], nums[j] = nums[j], nums[i]
                now_num = nums[i]
                i += 1
            j += 1
        return i
        