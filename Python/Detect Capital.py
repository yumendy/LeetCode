import string
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        self.upper_set = set(string.ascii_uppercase)
        self.lower_set = set(string.ascii_lowercase)
        return self.case_one(word) or self.case_two(word) or self.case_three(word)
        
    def case_one(self, word):
        return set(word).issubset(self.upper_set)
    def case_two(self, word):
        return set(word).issubset(self.lower_set)
    def case_three(self, word):
        return word[0] in self.upper_set and set(word[1:]).issubset(self.lower_set)
        
    