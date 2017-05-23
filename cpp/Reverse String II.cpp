class Solution {
public:
    string reverseStr(string s, int k) {
        auto start_index = s.begin();
        while (start_index < s.end()) {
            auto end_index = start_index + k > s.end() ? s.end() : start_index + k;
            reverse(start_index, end_index);
            start_index += 2 * k;
        }
        return s;
    }
};
