"""
Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
an additional temporary stack, but you may not copy the elements into any other data structure
(such as an array). The stack supports the following operations: push, pop, peek, and is Empty.
"""

from stack import stack

class sortStack(stack):
    def push(self, value):
        saveStack = stack()
        while value > self.peek() or self.isEmpty is False:
            saveStack.push(self.pop())
            if self.isEmpty():
                break
        self.values.append(value)
        while saveStack.isEmpty() is False:
            self.push(saveStack.pop())
            
def main():
    x = sortStack(5)
    x.push(1)
    x.push(10)
    return x