class stack():
    def __init__(self, startValue = None):
        self.values = [] # end of list is the top of the stack
        if startValue is not None:
            self.values.append(startValue)

    def pop(self):
        if self.isEmpty():
            raise ValueError('Stack is empty')
        else:
            out = self.values[-1]
            self.values = self.values[:-1]
            return out

    def push(self, value):
        self.values.append(value)

    def peek(self):
        if self.isEmpty():
            raise ValueError('Stack is empty')
        else:
            return self.values[-1]

    def isEmpty(self):
        if len(self.values) == 0:
            return True
        else:
            return False

    def min(self): #3.2 Stack Min - Operates in O(1)
        if self.isEmpty():
            raise ValueError('Stack is Empty')
        try:
            return min(self.values)
        except:
            raise ValueError("Stack has no minimum value")