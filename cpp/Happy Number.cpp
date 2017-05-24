class Solution {
public:
    bool isHappy(int n) {
        map<int, bool> mid_num;
        while (mid_num.find(n) == mid_num.end()) {
            mid_num[n] = true;
            vector<int> num_list;
            while (n > 0) {
                num_list.push_back(n % 10);
                n /= 10;
            }
            for (int num: num_list) {
                n += num * num;
            }
            if (n == 1) {
                return true;
            }
        }
        return false;
    }
};
