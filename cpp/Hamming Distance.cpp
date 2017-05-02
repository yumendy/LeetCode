class Solution {
public:
    int hammingDistance(int x, int y) {
        int counter = 0;
        int temp_num = x ^ y;
        while(temp_num > 0) {
            counter += temp_num & 1;
            temp_num >>= 1;
        }
        return counter;
    }
};
