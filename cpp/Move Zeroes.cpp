class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int zero_index = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i]) {
                swap(nums[zero_index], nums[i]);
                zero_index++;
            }
        }
    }
};
