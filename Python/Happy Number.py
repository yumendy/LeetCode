class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        mid_num = []
        
        
        while n not in mid_num:
            mid_num.append(n)
            num_list = []
            while n > 0:
                num_list.append(n % 10)
                n /= 10
            n = sum([num ** 2 for num in num_list])
            if n == 1:
                return True
        return False