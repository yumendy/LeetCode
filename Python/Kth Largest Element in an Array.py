class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.nums = nums
        self.build_heap(len(nums))
        self.heap_sort()
        return nums[k - 1]
    
    def build_heap(self, size):
        for idx in xrange((size - 1) / 2, -1, -1 ):
            self.tidy(idx, len(self.nums))
    
    def tidy(self, idx, size):
        small = idx
        if idx * 2 + 1 < size:
            if self.nums[small] > self.nums[idx * 2 + 1]:
                small = idx * 2 + 1
        if idx * 2 + 2 < size:
            if self.nums[small] > self.nums[idx * 2 + 2]:
                small = idx * 2 + 2
        if small != idx:
            self.nums[small], self.nums[idx] = self.nums[idx], self.nums[small]
            self.tidy(small, size)
    
    def heap_sort(self):
        for idx in xrange(len(self.nums) - 1, -1, -1):
            self.nums[0], self.nums[idx] = self.nums[idx], self.nums[0]
            self.tidy(0, idx)
