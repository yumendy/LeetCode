class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = None
        max2 = None
        max3 = None
        
        if len(nums) < 3:
            return max(nums)
        else:
            for num in nums:
                if num == max1 or num == max2 or num == max3:
                    continue
                elif max1 == None or num > max1:
                    max3 = max2
                    max2 = max1
                    max1 = num
                elif max2 == None or num > max2:
                    max3 = max2
                    max2 = num
                elif max3 == None or num > max3:
                    max3 = num
            return max3 if max3 != None else max1
