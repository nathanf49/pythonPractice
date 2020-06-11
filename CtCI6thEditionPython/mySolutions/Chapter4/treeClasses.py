class node:
    """
    Holds a value and can hold other nodes if it has children. Children must also be nodes
    Example:
        node0 = node(value, [node(value1), node(value2)]
        creates a node that holds value and has children that are nodes holding value1 and value2
    """

    def __init__(self, value, children=None):
        if type(value) is not int:
            raise ValueError('Values must be integers')
        self.value = value  # assigns data to node of tree
        self.children = []  # list of children if there are any
        self.parent = None
        if children is not None:  # does not keep list if there are no children
            if type(children) is node:  # makes sure all children are also tree nodes
                self.children.append(children)
                children.parent = self
            elif type(children) is list:
                for child in children:
                    if type(child) is not node:
                        raise TypeError("Children must be nodes")  # Throes error if child in list is not node
                    self.children.append(child)
                    child.parent = self
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
            child.parent = self
        elif type(child) is binaryNode:  # binary nodes can only have 2 children
            if len(self.children) >= 2:
                raise Exception("Binary nodes can only have 2 children")
            else:
                self.children.append(child)
                child.parent = self

        else:
            raise TypeError('Please put your value in a node to add it as a child')

    def __str__(self):
        return 'Value' + str(self.value) + ' Parent: ' + str(self.parent)


class binaryNode(node):
    """
    Similar to a regular node, but has a maximum of 2 children
    """

    def __init__(self, value, child0=None, child1=None):
        node.__init__(self, value)
        self.children = []  # list of children if there are any
        self.parent = None
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

    def __str__(self):
        if self.parent is not None:
            if len(self.children) == 0:
                out = 'Value: ' + str(self.value) + ', Parent: ' + str(self.parent.value)
            elif len(self.children) == 1:
                out = 'Value: ' + str(self.value) + ', Parent: ' + str(self.parent.value
                                                                       ) + ', Child 0: ' + str(self.children[0].value)
            else:
                out = 'Value: ' + str(self.value) + ', Parent: ' + str(self.parent.value) + ', Child 0: ' + str(
                    self.children[0].value) + ', Child 1: ' + str(self.children[1].value)
        else:
            if len(self.children) == 0:
                out = 'Value: ' + str(self.value)
            elif len(self.children) == 1:
                out = 'Value: ' + str(self.value) + ', Parent: None' + ', Child 0: ' + str(self.children[0].value)
            else:
                out = 'Value: ' + str(self.value) + ', Parent: None' + ', Child 0: ' + str(self.children[0].value
                                                                                           ) + ' Child 1: ' + str(
                    self.children[1].value)
        return out


class binarySearchNode(binaryNode):
    """
    Similar to binaryNode, but all left values must be less than or equal to all allParentValues and all right values
    must be greater than all allParentValues
    """

    def __init__(self, value, child0=None, child1=None):
        if type(value) is not (int or float):
            raise Exception("Please only use numerical values in Binary Search Trees to assist with sorting")
        if child0 is not None:  # makes sure children satisfy definition of binary search tree
            if child0.value > value:
                raise ValueError("Left child must be smaller than or equal to allParentValue value")
        if child1 is not None:  # makes sure children satisfy definition of binary search tree
            if child1.value <= value:
                raise ValueError("Right child must be larger than allParentValue value")
        binaryNode.__init__(self, value, child0=None, child1=None)
        self.children.sort()  # sorts child values so smaller value is on the left

    def addChild(self, child):
        if type(child) is not binarySearchNode:
            raise TypeError('Children must be binary search nodes')

        if len(self.children) >= 2:
            raise Exception("Binary nodes can only have 2 children")

        if child.value > self.value:  # child is the right side value
            self.rightSideCheck(child)
        else:  # child is left side value
            self.leftSideCheck(child)

        self.children.append(child)
        child.parent = self

        if len(self.children) == 2:  # re-sort values after a new one is added
            if self.children[0].value > self.children[1].value:  # swaps children if smaller child isn't on the left
                self.children[0], self.children[1] = self.children[1], self.children[0]

    def inOrderTraversal(self):  # prints values in order from smallest to largest
        # wouldn't be in order on any other tree
        if len(self.children) > 0:
            self.children[0].inOrderTraversal()
        print(self.value)
        if len(self.children) == 2:
            self.children[1].inOrderTraversal()


    ### FIXME this check breaks when a parent is on a different side than the added node will be on
    def leftSideCheck(self, child):  # checks that all values above inserted value are less than inserted value
        child.parent = self
        current = child  # creates a variable for going through parent values
        while current.parent is not None:  # goes through all parents to root and makes sure child is less than those
            if current.parent.value < child.value:
                child.parent = None
                raise ValueError('Left side values must be less than or equal to all parent values')
            current = current.parent

    def rightSideCheck(self, child):  # checks that all values above inserted value are less than inserted value
        child.parent = self
        current = child  # creates a variable for going through parent values
        while current.parent is not None:  # goes through all parents to root and makes sure child is greater than those
            if current.parent.value >= child.value:
                child.parent = None
                raise ValueError('Right side values must be greater than all parent values')
            current = current.parent

    def __str__(self):
        return binaryNode.__str__(self)


# Testing nodes
'''
n0 = binarySearchNode(0)
n1 = binarySearchNode(1)
n2 = binarySearchNode(2)
n3 = binarySearchNode(3)
n4 = binarySearchNode(4)
n5 = binarySearchNode(5)
n6 = binarySearchNode(6)
n7 = binarySearchNode(7)
n8 = binarySearchNode(8)
n9 = binarySearchNode(9)
n10 = binarySearchNode(10)
n11 = binarySearchNode(11)
n12 = binarySearchNode(12)
n13 = binarySearchNode(13)
n14 = binarySearchNode(14)
n15 = binarySearchNode(15)
n16 = binarySearchNode(16)
n17 = binarySearchNode(17)
n18 = binarySearchNode(18)
n19 = binarySearchNode(19)
n20 = binarySearchNode(20)
n100 = binarySearchNode(100)

n10.addChild(n5)
n10.addChild(n17)
n5.addChild(n8)
n5.addChild(n3)
n3.addChild(n1)
n3.addChild(n4)
n17.addChild(n19)
n17.addChild(n12)
n12.addChild(n11)
n19.addChild(n18)
n19.addChild(n20)
'''