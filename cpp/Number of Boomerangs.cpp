class Solution {
public:
    int numberOfBoomerangs(vector<pair<int, int>>& points) {
        int result = 0;
        for (auto point : points) {
            map<int, int> dis_dic;
            for (auto point_b : points) {
                int dis = compute_dis(point, point_b);
                if (dis_dic.find(dis) != dis_dic.end()) {
                    dis_dic[dis]++;
                } else {
                    dis_dic[dis] = 1;
                }
            }
            for (auto p : dis_dic) {
                result += p.second * (p.second - 1);
            }
        }
        return result;
    }

    int compute_dis(pair<int, int> a, pair<int, int> b) {
        return (a.first - b.first) * (a.first - b.first) + (a.second - b.second) * (a.second - b.second);
    }
};
