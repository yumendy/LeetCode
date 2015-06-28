class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n < 2:
            return 0
        else:
            lst = [0]
            lst += [1] * (n - 1)
            lst[1] = 0
            for i in xrange(2, n):
                if lst[i] == 1:
                    for j in xrange(i ** 2, n, i):
                        lst[j] = 0
            return sum(lst)