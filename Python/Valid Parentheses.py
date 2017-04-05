class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        else:
            dic = {
                ')':'(',
                ']':'[',
                '}':'{'
                }
            stack = []
            for ch in s:
                if ch in '([{':
                    stack.append(ch)
                else:
                    if (not stack) or (stack.pop() != dic[ch]):
                        return False
            return stack == []
        