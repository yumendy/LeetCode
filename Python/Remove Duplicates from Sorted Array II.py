class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if len(nums) < 3:
            return len(nums)
        else:
            Sum = 0
            temp = nums[0]
            count = 0
            lst = []
            for item in nums:
                if item == temp:
                    if count < 2:
                        count += 1
                else:
                    Sum += count
                    lst += [temp] * count
                    temp = item
                    count = 1
            nums = lst
            return Sum + count

s = Solution()

print s.removeDuplicates([1,1,1,2])