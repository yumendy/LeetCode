class Solution {
public:
    bool isUgly(int num) {
        for (int fact : vector<int> {2,3,5}) {
            while (num > 0 && num % fact == 0) {
                num /= fact;
            }
        }
        return num == 1;
    }
};
