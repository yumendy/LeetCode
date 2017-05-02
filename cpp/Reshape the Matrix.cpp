class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& nums, int r, int c) {
        int sum_counter = 0;
        for (vector<int> row : nums) {
            sum_counter += row.size();
        }
        if (sum_counter < r * c)
            return nums;
        else {
            vector<vector<int>> result;
            vector<int> temp;
            for (vector<int> row : nums) {
                for (int num : row) {
                    temp.push_back(num);
                    if (temp.size() == c) {
                        result.push_back(temp);
                        temp = vector<int>();
                    }
                }
            }
            return result;
        }
    }
};
