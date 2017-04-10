class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        c = Counter(nums)
        self.nums = [item for item in c.iteritems()]
        self.heap_build(len(self.nums))
        self.heap_sort()
        return [item[0] for item in self.nums[:k]]

    def heap_build(self, size):
        for idx in xrange((size - 1) / 2, -1, -1):
            self.tidy(idx, size)

    def tidy(self, idx, size):
        small = idx
        if idx * 2 + 1 < size:
            if self.nums[small][1] > self.nums[idx * 2 + 1][1]:
                small = idx * 2 + 1
        if idx * 2 + 2 < size:
            if self.nums[small][1] > self.nums[idx * 2 + 2][1]:
                small = idx * 2 + 2
        if small != idx:
            self.nums[small], self.nums[idx] = self.nums[idx], self.nums[small]
            self.tidy(small, size)

    def heap_sort(self):
        for idx in xrange(len(self.nums) - 1, -1, -1):
            self.nums[0], self.nums[idx] = self.nums[idx], self.nums[0]
            self.tidy(0, idx)
