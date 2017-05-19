class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        map<int, bool> counter;
        for(int num: nums) {
            if (counter.find(num) != counter.end()) {
                return true;
            } else {
                counter[num] = true;
            }
        }
        return false;
    }
};
