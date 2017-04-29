class Solution {
public:
    int findComplement(int num) {
        int temp = 0;
        int index = 0;
        while (num >> index)
        {
            temp |= (((num >> index) & 0x1) != 0 ? 0 : 1) << index;
            index++;
        }
        return temp;
    }
};
