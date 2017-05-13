class Solution {
public:
    int minMoves(vector<int>& nums) {
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        return sum - nums.size() * *min_element(nums.begin(), nums.end());
    }
};
