class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        result = 0
        for point in points:
            dis_dic = {}
            for point_b in points:
                dis = self.compute_dis(point, point_b)
                if dis in dis_dic:
                    dis_dic[dis] += 1
                else:
                    dis_dic[dis] = 1
            for key in dis_dic:
                result += dis_dic[key] * (dis_dic[key] - 1)
        return result
                
    
    
    def compute_dis(self, a, b):
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
                
            