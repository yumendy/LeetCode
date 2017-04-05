class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        num = '1'
        for i in xrange(n - 1):
            num = self.get_next_num(num)
        return num
    
    def get_next_num(self, num):
        result = []
        counter = 0
        current_char = num[0]
        for i in num:
            if i == current_char:
                counter += 1
            else:
                result.append(str(counter)+current_char)
                current_char = i
                counter = 1
        result.append(str(counter)+current_char)
        return ''.join(result)
