class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.temp = [0]
        for num in nums:
            self.temp.append(self.temp[-1] + num)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.temp[j + 1] - self.temp[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)