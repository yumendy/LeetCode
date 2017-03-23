class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        self.line1 = set([i for i in 'qwertyuiop'])
        self.line2 = set([i for i in 'asdfghjkl'])
        self.line3 = set([i for i in 'zxcvbnm'])
        return [i for i in words if self.in_one_line(i)]
    
    def in_one_line(self, word):
        word_set = set([i for i in word.lower()])
        if len(word_set | self.line1) == len(self.line1):
            return True
        elif len(word_set | self.line2) == len(self.line2):
            return True
        elif len(word_set | self.line3) == len(self.line3):
            return True
        else:
            return False
        
        