class Solution {
public:
    int addDigits(int num) {
        int temp = num;
        while (temp > 9) {
            temp = 0;
            while (num > 0) {
                temp += num % 10;
                num /= 10;
            }
            num = temp;
        }
        return temp;
    }
};
