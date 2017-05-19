class Solution {
public:
    int longestPalindrome(string s) {
        map<char, size_t> counter;
        for (char ch: s) {
            if (counter.find(ch) != counter.end()) {
                counter[ch] ++;
            } else {
                counter[ch] = 1;
            }
        }
        int sum = 0;
        int odd_flag = 0;
        for (auto i = counter.begin(); i != counter.end(); i++) {
            if (i->second % 2 == 0) {
                sum += i->second;
            } else {
                odd_flag = 1;
                sum += i->second - 1;
            }
        }
        return sum + odd_flag;
    }
};
