class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end());
        sort(s.begin(),s.end());
        int counter = 0;
        auto g_pointer = g.begin();
        auto s_pointer = s.begin();
        while (g_pointer != g.end() && s_pointer != s.end()) {
            if (*s_pointer >= *g_pointer) {
                g_pointer++;
                counter++;
            }
            s_pointer++;
        }
        return counter;
    }
};
