class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums == []:
            return 0
        else:
            pre = 0
            post = len(nums) - 1
            while pre != post:
                if nums[pre] == val:
                    if nums[post] != val:
                        nums[pre], nums[post] = nums[post], nums[pre]
                        pre += 1
                    else:
                        post -= 1
                else:
                    pre += 1
            if nums[pre] == val:
                return pre
            else:
                return pre + 1    
            