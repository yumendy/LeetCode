class Solution {
public:
    int romanToInt(string s) {
        map<char, int> values;
        values['I'] = 1;
        values['V'] = 5;
        values['X'] = 10;
        values['L'] = 50;
        values['C'] = 100;
        values['D'] = 500;
        values['M'] = 1000;

        int num = 0;

        for (int i = 0; i < s.size() - 1; ++i) {
            if (values[s[i]] < values[s[i + 1]]) {
                num -= values[s[i]];
            } else {
                num += values[s[i]];
            }
        }
        return num + values[s[s.size() - 1]];
    }
};
