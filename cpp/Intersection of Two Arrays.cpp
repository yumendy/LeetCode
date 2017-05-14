class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        vector<int> result;
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        int last_insert_num = INFINITY;
        for (auto i = nums1.begin(), j = nums2.begin(); i < nums1.end() && j < nums2.end() ;) {
            if (*i == *j && *i != last_insert_num) {
                result.push_back(*i);
                last_insert_num = *i;
            } else {
                if (*i < *j) {
                    i++;
                } else {
                    j++;
                }
            }
        }
        return result;
    }
};
