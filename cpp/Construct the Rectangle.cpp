class Solution {
public:
    vector<int> constructRectangle(int area) {
        vector<int> result;
        for (int i = (int) sqrt(area); i < area + 1; ++i) {
            if (area % i == 0) {
                result.push_back(max(area / i, i));
                result.push_back(min(area / i, i));
                break;
            }
        }
        return result;
    }
};
