class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        alphanumeric = "abcdefghijklmnopqrstuvwxyz0123456789"
        s = s.lower()
        temp = []
        for letter in s:
            if letter in alphanumeric:
                temp.append(letter)
        result = "".join(temp)
        return result == result[::-1]
