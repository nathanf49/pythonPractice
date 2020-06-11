from treeClasses import binaryNode

class minHeap:
    def __init__(self, root):
        if type(root) is not binaryNode: # if root is not binary node, attempts to cast it as one
            if type(root) is int or type(root) is float:
                root = binaryNode(root)
            else:
                raise TypeError("Root must be a numerical value")
        self.root = root

x= minHeap(5)