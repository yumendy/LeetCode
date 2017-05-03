class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int max = 0;
        int counter = 0;
        for (int temp : nums) {
            if (temp) {
                counter++;
            } else {
                max = max > counter ? max : counter;
                counter = 0;
            }
        }
        max = max > counter ? max : counter;
        return max;
    }
};
