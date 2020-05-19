class node:
    def __init__(self, value, children=None):
        self.value = value  # assigns data to node of tree
        self.children = []  # list of children if there are any
        if children is not None:  # does not keep list if there are no children
            if type(children) is node:  # makes sure all children are also tree nodes
                self.children.append(children)
            elif type(children) is list:
                for child in children:
                    if type(child) is not node:
                        raise TypeError("Children must be nodes") # Throes error if child in list is not node
                    self.children.append(child)
            else:
                raise TypeError("Children must be nodes") # Throws error for single child that isn't node

    def __str__(self):
        return self.value

    def showChildValues(self):
        if type(self.children) is list:
            out = []
            for current in self.children:
                out.append(current.value)
            return out
        else:
            return self.value

class tree:
    def __init__(self, root):
        if type(root) is not node:
            self.root = node(root)
        else:
            self.root = root

    def __str__(self):
        return node.__str__(self.root)