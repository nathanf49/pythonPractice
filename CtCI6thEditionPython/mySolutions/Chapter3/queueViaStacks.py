"""
Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.
"""
from stack import stack

class myQueue:
    def __init__(self, startingValue = None):
        self.stack = stack(startingValue) # makes a stack to store values

    def add(self, value):
        self.stack.push(value)

    def pull(self):
        if self.isEmpty():
            raise ValueError('Queue is empty')
        queue = stack()
        while self.stack.isEmpty() is False: # reverses stack into a queue
            queue.push(self.stack.pop())
        out = queue.pop()
        while queue.isEmpty() is False:
            self.stack.push(queue.pop())
        return out

    def peek(self):
        if self.isEmpty():
            raise ValueError('Queue is empty')
        queue = stack()
        while self.stack.isEmpty() is False: # reverses stack into a queue
            queue.push(self.stack.pop())
        out = queue.peek()
        while queue.isEmpty() is False:
            self.stack.push(queue.pop())
        return out

    def isEmpty(self):
        return self.stack.isEmpty()

def main():
    queue = myQueue(1)
    queue.add(2)
    queue.add(3)
    return queue