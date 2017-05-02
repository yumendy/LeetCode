class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& findNums, vector<int>& nums) {
        vector<int> result;

        for (int find_num : findNums) {
            vector<int>::iterator index = find(nums.begin(), nums.end(), find_num);
            bool find_flag = false;
            for (vector<int>::iterator i = index; i < nums.end(); ++i) {
                if (*i > find_num) {
                    result.push_back(*i);
                    find_flag = true;
                    break;
                }
            }
            if (!find_flag) {
                result.push_back(-1);
            }
        }
        return result;
    }
};
