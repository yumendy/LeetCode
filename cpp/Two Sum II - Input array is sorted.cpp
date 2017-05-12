class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        map<int, int> dict;
        vector<int> result;
        for (int i = 0; i < numbers.size(); ++i) {
            if (dict.find(target - numbers[i]) != dict.end()) {
                result.push_back(dict[target- numbers[i]]);
                result.push_back(i + 1);
                break;
            } else {
                dict[numbers[i]] = i + 1;
            }
        }
        return result;
    }
};
