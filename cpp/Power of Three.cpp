class Solution {
public:
    bool isPowerOfThree(int n) {
        if (n <= 0)
            return false;
        else {
            while (!(n % 3)) {
                n /= 3;
            }
            return n == 1 || n == 0;
        }
    }
};
