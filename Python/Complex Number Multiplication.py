class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return self.complexNumber(a) * self.complexNumber(b)
    
    class complexNumber(object):
        def __init__(self, s):
            self.r, self.i = tuple(s[:-1].split('+'))
            self.r = int(self.r)
            self.i = int(self.i)
    
        def __mul__(self, other):
            new_r = self.r * other.r + (-1) * self.i * other.i
            new_i = self.r * other.i + self.i * other.r
            return '%d+%di' % (new_r, new_i)
