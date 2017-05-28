class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        if (nums.size() == 0) {
            return 0;
        } else {
            for (size_t idx = 0; idx < nums.size(); idx++) {
                if (target <= nums[idx]) {
                    return idx;
                }
            }
            return nums.size();
        }
    }
};
