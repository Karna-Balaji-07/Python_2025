# Min stack

class MinStack(object):

    def __init__(self):
        self.arr = []
        self.minStack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.arr.append(val)
        if not self.minStack or self.minStack[-1] >= val:
            self.minStack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        if self.arr[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.arr.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.arr[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()