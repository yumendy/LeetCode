class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int counter = 0;
        for (int i = 0; i + 1 < prices.size(); ++i) {
            if (prices[i + 1] > prices[i]) {
                counter += (prices[i + 1] - prices[i]);
            }
        }
        return counter;
    }
};
