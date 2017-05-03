class Solution {
public:
    bool detectCapitalUse(string word) {
        unsigned int state = 0;
        for (char ch: word) {
            this->tran(state, ch);
            if (state == 5) {
                return false;
            }
        }
        return true;
    }
    void tran(unsigned int &state, char ch) {
        switch (state) {
            case 0: {
                if (ch >= 'a' && ch <= 'z') {
                    state = 1;
                } else {
                    state = 2;
                }
                break;
            }
            case 1: {
                if (ch >= 'A' && ch <= 'Z') {
                    state = 5;
                }
                break;
            }
            case 2: {
                if (ch >='a' && ch <= 'z') {
                    state = 3;
                } else {
                    state = 4;
                }
                break;
            }
            case 3: {
                if (ch >= 'A' && ch <= 'Z') {
                    state = 5;
                }
                break;
            }
            case 4: {
                if (ch >= 'a' && ch <= 'z') {
                    state = 5;
                }
                break;
            }
            default:
                state = 5;
        }
    }
};
