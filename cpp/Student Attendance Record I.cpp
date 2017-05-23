class Solution {
public:
    bool checkRecord(string s) {
        return count(s.begin(), s.end(), 'A') < 2 and s.find("LLL") == string::npos;
    }
};
