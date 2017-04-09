class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.size = 0
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.size:
            self.stack.append((x, x))
        else:
            s = min(x, self.getMin())
            self.stack.append((x, s))
        self.size += 1
            
            
        

    def pop(self):
        """
        :rtype: void
        """
        if self.size:
            self.stack.pop()
            self.size -= 1
        
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.size:
            return self.stack[-1][1]
        else:
            return None
            
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()