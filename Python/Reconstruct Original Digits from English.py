class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        c = Counter(s)
        zero_num = c['z']
        c.subtract('zero' * zero_num)
        six_num = c['x']
        c.subtract('six' * six_num)
        seven_num = c['s']
        c.subtract('seven' * seven_num)
        two_num = c['w']
        c.subtract('two' * two_num)
        five_num = c['v']
        c.subtract('five' * five_num)
        four_num = c['f']
        c.subtract('four' * four_num)
        one_num = c['o']
        c.subtract('one' * one_num)
        three_num = c['r']
        c.subtract('three' * three_num)
        eight_num = c['h']
        c.subtract('eight' * eight_num)
        ten_num = c['t']
        c.subtract('ten' * ten_num)
        nine_num = c['i']
        
        ans = '0' * zero_num + '1' * one_num + '2' * two_num + '3' * three_num + '4' * four_num + '5' * five_num + '6' * six_num + '7' * seven_num + '8' * eight_num + '9' * nine_num
        return ans
