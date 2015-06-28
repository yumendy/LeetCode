class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.s = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.s.append(x)

    # @return nothing
    def pop(self):
        self.s.pop()

    # @return an integer
    def top(self):
        return self.s[-1]

    # @return an boolean
    def empty(self):
        return True if len(self.s) == 0 else False