# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x:x.start)
        res = []
        temp = intervals[0]
        for item in intervals[1:]:
            if item.start <= temp.end and temp.end < item.end:
                temp.end = item.end
            elif item.start > temp.end:
                res.append(temp)
                temp = item
        res.append(temp)
        return res
