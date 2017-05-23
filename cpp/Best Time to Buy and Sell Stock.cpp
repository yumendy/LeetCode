class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() == 0)
            return 0;
        int max_profit = 0;
        int buy_price = prices[0];
        for (int price : prices) {
            max_profit = max(max_profit, price - buy_price);
            buy_price = min(buy_price, price);
        }
        return max_profit;
    }
};
