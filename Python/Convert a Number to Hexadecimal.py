class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0:
            return self.uint_to_hex(self.neg_to_uint(num))
        else:
            return self.uint_to_hex(num)
        
    def neg_to_uint(self, num):
        s = bin(num)[3:]
        l = len(s)
        s = '0' * (32 - l) + s
        s = ''.join(['1' if num == '0' else '0' for num in s])
        return int(s, 2) + 1
    
    def uint_to_hex(self, num):
        dic = dict(zip(range(16), '0123456789abcdef'))
        s = []
        if num == 0:
            return '0'
        while num > 0:
            s.append(dic[num % 16])
            num /= 16
        return ''.join(s)[::-1]