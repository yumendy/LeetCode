class Solution {
public:
    vector<string> readBinaryWatch(int num) {
        vector<string> result;
        string temp_str;
        char temp[6];
        for (unsigned char i = 0; i < 12; ++i) {
            for (unsigned char j = 0; j < 60; ++j) {
                if (count_bit(i) + count_bit(j) == num) {
                    sprintf(temp, "%d:%02d", i, j);
                    temp_str = temp;
                    result.push_back(temp_str);
                }
            }
        }
        return result;
    }

    unsigned char count_bit(unsigned char num) {
        num = (num &0x55) + ((num >> 1) & 0x55);
        num = (num &0x33) + ((num >> 2) & 0x33);
        num = (num &0x0f) + ((num >> 4) & 0x0f);
        return num;
    }
};
