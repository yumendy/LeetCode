class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        rl = list(ransomNote)
        ml = list(magazine)
        rl.sort()
        ml.sort()
        
        i = 0
        for ch in rl:
            for i in xrange(i, len(ml)):
                if ch == ml[i]:
                    i += 1
                    break
            else:
                break
        else:
            return True
        return False
            
        