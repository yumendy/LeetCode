class Solution {
public:
    int majorityElement(vector<int>& nums) {
        map<int, int> counter;
        for (int num : nums) {
            if (counter.find(num) != counter.end()) {
                counter[num]++;
            } else {
                counter[num] = 1;
            }
        }
        int max_key = 0, max_value = -INFINITY;
        for (auto iter = counter.begin(); iter != counter.end(); iter++) {
            if (iter->second > max_value) {
                max_value = iter->second;
                max_key = iter->first;
            }
        }
        return max_key;
    }
};
