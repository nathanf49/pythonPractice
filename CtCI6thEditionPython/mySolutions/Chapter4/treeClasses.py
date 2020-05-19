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
        if type(child) is node:
            self.children.append(child)

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

    def addChild(self, child):
        if type(child) is binaryNode or binarySearchNode:
            if len(self.children) < 2:
                self.children.append(child)


class binarySearchNode(binaryNode):  # TODO Ensure that all left child values are greater than all values above them
    """
    Similar to binaryNode, but all left values must be less than or equal to all parents and all right values must be
    greater than all parents
    """
    def __init__(self, value, child0=None, child1=None):
        if type(value) is not int or float:
            raise Exception("Please only use numerical values in Binary Search Trees to assist with sorting")
        if child0 > value:
            raise ValueError("Left child must be smaller than or equal to parent value")
        if child1 <= value:
            raise ValueError("Right child must be larger than parent value")
        binaryNode.__init__(self, value, child0=None, child1=None)
        self.parents = []
        self.children.sort()  # sorts child values so smaller value is on the left
        for child in self.children:
            if self.value not in child.parents:
                child.parents.append(self.value)

    def addChild(self, child): #TODO add left and add right might make this easier
        if len(self.children) == 1:
            if not (child <= self.value and self.children[0] > self.value) or (child > self.value and self.children[0] < child):
                raise ValueError("One child must be bigger than all parent values and one must be smaller or equal to")
        binaryNode.addChild(self, child)
        self.children.sort()  # re-sort values after a new one is added

    def inOrderTraversal(self):  # prints values in order from smallest to largest
        # wouldn't be in order on any other tree
        if len(self.children) > 0:
            self.children[0].inOrderTraversal(self)
        print(self.value)
        if len(self.children) == 2:
            self.children[1].inOrderTraversal(self)
