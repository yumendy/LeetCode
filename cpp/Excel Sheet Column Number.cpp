class Solution {
public:
    int titleToNumber(string s) {
        int  sum = 0;
        int power = 0;
        reverse(s.begin(), s.end());
        for (char ch : s) {
            sum += (ch - 'A' + 1) * pow(26, power++);
        }
        return sum;
    }
};
