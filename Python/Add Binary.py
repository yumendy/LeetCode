class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        a = int(a, 2)
        b = int(b, 2)
        c = a + b
        if c is 0:
            return '0'
        lst = []
        while c > 0:
            lst.append(c % 2)
            c /= 2
        lst.reverse()
        lst = map(str, lst)
        return ''.join(lst)
