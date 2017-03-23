class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return [str(i) if (i % 3 != 0 and i % 5 != 0) else 'FizzBuzz' if (i % 15 == 0) else ('Fizz' if i % 3 == 0 else 'Buzz') for i in xrange(1, n + 1)]