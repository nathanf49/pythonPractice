class node:
    """
    Holds a value and can hold other nodes if it has children. Children must also be nodes
    Example:
        node0 = node(value, [node(value1), node(value2)]

        creates a node that holds value and has children that are nodes holding value1 and value2
    """

    def __init__(self, value, children=None):
        self.value = value  # assigns data to node of tree
        self.children = []  # list of children if there are any
        if children is not None:  # does not keep list if there are no children
            if type(children) is node:  # makes sure all children are also tree nodes
                self.children.append(children)
            elif type(children) is list:
                for child in children:
                    if type(child) is not node:
                        raise TypeError("Children must be nodes")  # Throes error if child in list is not node
                    self.children.append(child)
            else:
                raise TypeError("Children must be nodes")  # Throws error for single child that isn't node

    def showChildValues(self):
        out = []
        for current in self.children:
            out.append(current.value)
        return out

    def addChild(self, child):
        if type(child) is node:  # adds node since tree can have any number of children
            self.children.append(child)
        elif type(child) is binaryNode or binarySearchNode:  # binary nodes can only have 2 children
            if len(self.children) < 2:
                self.children.append(child)
            else:
                raise Exception("Binary nodes can only have 2 children")
        else:
            raise TypeError('Please put your value in a node to add it as a child')

    def __str__(self):
        return str(self.value)


class binaryNode(node):
    """
    Similar to a regular node, but has a maximum of 2 children
    """

    def __init__(self, value, child0=None, child1=None):
        node.__init__(self, value)
        self.children = []  # list of children if there are any
        if child0 is not None:  # does not keep list if there are no children
            if type(child0) is binaryNode or binarySearchNode:  # makes sure all children are also tree nodes
                self.children.append(child0)
            else:
                raise TypeError("Child0 must be a binary node")  # Throws error for non binary node

        if child1 is not None:  # does not keep list if there are no children
            if type(child1) is binaryNode or binarySearchNode:  # makes sure all children are also tree nodes
                self.children.append(child1)
            else:
                raise TypeError("Child1 must be a binary node")  # Throws error for non binary node


class binarySearchNode(binaryNode):
    """
    Similar to binaryNode, but all left values must be less than or equal to all parents and all right values must be
    greater than all parents
    """

    def __init__(self, value, child0=None, child1=None):
        if type(value) is not (int or float):
            raise Exception("Please only use numerical values in Binary Search Trees to assist with sorting")
        if child0 is not None:  # makes sure children satisfy definition of binary search tree
            if child0 > value:
                raise ValueError("Left child must be smaller than or equal to parent value")
        if child1 is not None:  # makes sure children satisfy definition of binary search tree
            if child1 <= value:
                raise ValueError("Right child must be larger than parent value")
        binaryNode.__init__(self, value, child0=None, child1=None)
        self.parents = []
        self.children.sort()  # sorts child values so smaller value is on the left
        for child in self.children:
            child.parents = self.parents
            if self.value not in child.parents:  # makes sure children have parents recorded
                child.parents.append(self.value)

    def addChild(self, child):
        if len(self.children) == 1:
            if not (child.value <= self.value and child.value < self.children[0].value and child.value <= min(self.parents)) or (child.value > self.value and self.children[0].value < child.value and child.value > max(self.parents)):
                # Ensures that child is less than or equal to all parent values if it will be on the left and greater
                # than all parent values to the right
                raise ValueError("One child must be bigger than all parent values and one must be smaller or equal to")
        node.addChild(self, child)
        self.children[-1].parents = self.parents  # saves own parents as parents of new child
        if self.value not in self.children[-1].parents:  # adds own value to child's parent values #FIXME root adds itself to parents
            self.children[-1].parents.append(self.value)
        if len(self.children) == 2:  # re-sort values after a new one is added
            if self.children[0].value > self.children[1].value: # swaps children if smaller child isn't on the left
                self.children[0], self.children[1] = self.children[1], self.children[0]


    def inOrderTraversal(self):  # prints values in order from smallest to largest
        # wouldn't be in order on any other tree
        if len(self.children) > 0:
            self.children[0].inOrderTraversal(self)
        print(self.value)
        if len(self.children) == 2:
            self.children[1].inOrderTraversal(self)


x = binarySearchNode(7)
y = binarySearchNode(8)
z = binarySearchNode(5)
