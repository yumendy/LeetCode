class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        counter = 0
        for i in xrange(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                counter += prices[i + 1] - prices[i]
        return counter