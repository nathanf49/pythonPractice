from stack import stack
"""
Describe how you could use a single array to implement three stacks.
"""

stack1 = stack(1)
stack1.push(1.1)
stack2 = stack(2)
stack2.push(2.2)
stack3 = stack(3)
stack3.push(3.3)
multiStack = []
multiStack.append(stack1)
multiStack.append(stack2)
multiStack.append(stack3)