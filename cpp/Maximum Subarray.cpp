class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max_sum = -INFINITY;
        int array_sum = 0;
        for (int num : nums) {
            if (array_sum > 0) {
                array_sum += num;
            } else {
                array_sum = num;
            }
            if (array_sum > max_sum)
                max_sum = array_sum;
        }
        return max_sum;
    }
};
