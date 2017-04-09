class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        elif num == 1:
            return [0,1]
        else:
            ans = [0, 1]
            group = 1
            for num in xrange(2, num + 1):
                if num == 2 ** group:
                    idx_gap = 2 ** group
                    group += 1
                ans.append(ans[num - idx_gap] + 1)
            return ans
