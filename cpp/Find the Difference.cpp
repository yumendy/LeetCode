class Solution {
public:
    char findTheDifference(string s, string t) {
        multiset<char> set_s, set_t, set_result;
        set_s.insert(s.begin(),s.end());
        set_t.insert(t.begin(), t.end());
        set_difference(set_t.begin(),set_t.end(), set_s.begin(), set_s.end(), insert_iterator<multiset<char>>(set_result,set_result.begin()));
        return *set_result.begin();
    }
};
