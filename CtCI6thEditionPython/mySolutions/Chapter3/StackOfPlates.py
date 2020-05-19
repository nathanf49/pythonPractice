"""
Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure S e t O f S t a c k s that mimics this. S e t O f S t a c k s should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
S e t O f S t a c k s . p u s h ( ) and S e t O f S t a c k s . p o p ( ) should behave identically to a single stack
(that is, p o p ( ) should return the same values as it would if there were just a single stack).
FOLLOW UP
Implement a function p o p A t ( i n t i n d e x ) which performs a pop operation on a specific sub-stack.
"""
from stack import stack


class plateStack:
    def __init__(self, capacity, startValue=None):
        self.capacity = capacity  # sets maximum number of objects in each substack
        self.stacks = []  # holds individual stacks
        if startValue is None:  # makes first substack
            substack = stack()
        else:
            substack = stack(startValue)
        self.stacks.append(substack)

    def pop(self):
        if self.isEmpty():
            raise ValueError('Stack is empty')
        else:
            out = self.stacks[-1].pop()  # pops value from last stack into out
            if self.stacks[-1].isEmpty():  # if that empties last stack, remove it
                self.stacks = self.stacks[:-1]
            return out

    def push(self, value):
        if len(self.stacks[-1].values) < self.capacity:  # pushes value onto last stack if it isn't a capacity yet
            self.stacks[-1].push(value)
        else:
            substack = stack(value)  # creates new stack with value and and makes that the new last stack in the
            # stack of plates
            self.stacks.append(substack)

    def peek(self):
        if self.isEmpty():
            raise ValueError('Stack is empty')
        else:
            return self.stacks[-1].peek()

    def popAt(self, stackNum):
        try: # gets substack if the stack to popAt exists
            substack = self.stacks[stackNum]
        except:
            raise ValueError('Stack ' + str(stackNum) + " doesn't exist.")

        out = substack.pop()  # pops value from last stack into out
        if substack.isEmpty():  # if that empties last stack, remove it
            self.stacks.remove(substack)
        return out

    def isEmpty(self):
        if len(self.stacks) == 0 or len(self.stacks[0].values) == 0:
            return True
        else:
            return False


def main():  # testing
    plates = plateStack(2)  # creates stack with capacity of 2
    print(plates.isEmpty())  # should be True
    plates.push(1)  # should push initial value into a substack
    print(plates.isEmpty())  # should be False, 1 was pushed onto the stack
    plates.push(2)
    plates.push(3)  # creates second stack
    plates.push(4)
    plates.push(5)  # creates third stack
    return plates
    print(plates.peek())  # should print 5, the last value pushed
    print(plates.pop())  # 5
    print(plates.pop())  # 4
    print(plates.pop())  # 3
    print(plates.pop())  # 2
    print(plates.pop())  # 1
    #print(plates.pop())  # Value Error, stack is Empty
