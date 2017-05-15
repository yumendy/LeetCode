class Solution {
public:
    int firstUniqChar(string s) {
        unsigned int counter[26];
        memset(counter, 0, sizeof(counter));
        for (char ch : s) {
            counter[ch - 'a']++;
        }
        for (int i = 0; i < s.size(); i++) {
            if (counter[s[i] - 'a'] == 1) {
                return i;
            }
        }
        return -1;
    }
};
