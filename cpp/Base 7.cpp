class Solution {
public:
    string convertToBase7(int num) {

        if (num == 0) {
            return string(1, '0');
        }

        bool flag;
        flag = num < 0;
        num = abs(num);
        vector<int> result;
        while (num > 0) {
            result.push_back(num % 7);
            num /= 7;
        }
        string string1;
        if (flag) {
            string1.push_back('-');
        }
        for (auto i = result.rbegin(); i != result.rend(); i++) {
            string1 += to_string(*i);
        }
        return string1;
    }
};
