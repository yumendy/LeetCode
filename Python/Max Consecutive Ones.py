class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_counter = 0
        counter = 0
        for num in nums:
            if num == 0:
                if counter > max_counter:
                    max_counter = counter
                counter = 0
            else:
                counter += 1
            
        return max_counter if max_counter > counter else counter
                