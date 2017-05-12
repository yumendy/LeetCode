class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& nums) {
        vector<int> lst = nums;
        vector<string> rank;
        sort(lst.begin(), lst.end(), greater_equal<int>());
        rank.push_back(string("Gold Medal"));
        rank.push_back(string("Silver Medal"));
        rank.push_back(string("Bronze Medal"));
        for (int i = 4; i < nums.size() + 1; ++i) {
            rank.push_back(to_string(i));
        }
        map<int, string> temp;
        for (int j = 0; j < lst.size(); ++j) {
            temp[lst[j]] = rank[j];
        }
        vector<string> result;
        for (int num : nums) {
            result.push_back(temp[num]);
        }
        return result;
    }
};
