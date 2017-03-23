class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        for l in xrange(int(area ** 0.5), area +1):
            if area % l == 0:
                return [max(l , area / l), min(l , area/ l)]
        