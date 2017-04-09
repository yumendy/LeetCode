class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        heaters.insert(0, float('-inf'))
        heaters.append(float('inf'))
        idx = 0
        res = 0
        for house in houses:
            while heaters[idx + 1] < house:
                idx += 1
            res = max(res, min(house - heaters[idx], heaters[idx + 1] - house))
        return res
