class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        sort(ransomNote.begin(), ransomNote.end());
        sort(magazine.begin(), magazine.end());
        int idx = 0;
        bool jump_flag = true;
        for (char ch : ransomNote) {
            bool flag = true;
            for (; idx < magazine.size(); ++idx) {
                if (ch == magazine[idx]) {
                    idx++;
                    flag = false;
                    break;
                }
            }
            if (flag) {
                jump_flag = false;
                break;
            }
        }
        return jump_flag;
    }
};
