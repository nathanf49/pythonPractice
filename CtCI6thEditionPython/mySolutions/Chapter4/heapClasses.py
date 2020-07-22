from treeClasses import binaryNode

class minHeap:
    def __init__(self, root):
        if type(root) is not binaryNode: # if root is not binary node, attempts to cast it as one
            if type(root) is int or type(root) is float:
                root = binaryNode(root)
            else:
                raise TypeError("Root must be a numerical value")
        else: # make sure root contains a number
            if type(root.value) is not int and type(root.value) is not float:
                raise TypeError("Root node must contain a number")
        self.root = root

    def insert(self, newNode):
        if type(newNode) is not binaryNode: # if input is not a binary node, attempt to cast it if value is a number
            if type(newNode) is int or type(newNode) is float:
                newNode = binaryNode(newNode)
            else:
                TypeError("The new node must be a binary node containing a number")
        else: # if new Node is a binary Node, make sure it contains a number
            if type(newNode.value) is not int and type(newNode.value) is not float:
                raise TypeError("New node must contain a number")
        self.children.append(newNode)


    

    def findOpen(self): #finds the first node with a position to allow a child
        current = self.root
        while len(current.children) == 2: # while current level of graph is full, move to next level
            current = current.children[1]


x= minHeap(5)
x.insert(7)