class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        max_profit = 0
        buy_price = prices[0]
        for i in prices:
            max_profit = max(max_profit, i - buy_price)
            buy_price = min(buy_price, i)
        return max_profit
        