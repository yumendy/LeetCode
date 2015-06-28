class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if len(nums) == 0:
            return []
        else:
            ranges = []
            start = end = nums[0]
            for item in nums:
                if item == end + 1:
                    end = item
                elif item > end + 1:
                    if end > start:
                        ranges.append("%d->%d" % (start, end))
                    else:
                        ranges.append(str(start))
                    start = end = item
            if end > start:
                ranges.append("%d->%d" % (start, end))
            else:
                ranges.append(str(start))
            return ranges