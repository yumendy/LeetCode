class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.stack_tail = []
        self.stack_head = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        while self.stack_head != []:
            self.stack_tail.append(self.stack_head.pop())
        self.stack_tail.append(x)
        self.size += 1
            
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while self.stack_tail != []:
            self.stack_head.append(self.stack_tail.pop())
        self.size -= 1
        return self.stack_head.pop()
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        while self.stack_tail != []:
            self.stack_head.append(self.stack_tail.pop())
        return self.stack_head[-1]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.size
        
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()