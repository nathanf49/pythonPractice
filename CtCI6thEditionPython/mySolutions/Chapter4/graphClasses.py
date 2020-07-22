class node:
    def __init__(self, value, connections = None):
        # Initialize Value
        if value is not None:
            self.value = value # import value of node
        else:
            raise TypeError('Nodes should have a value')

        # Initializing connections to other nodes
        self.connections = []  # initialize blank list of connections
        if connections is not None:
            if type(connections) is node: # if node has one connection to another node
                self.connections = [connections] # adds listed node as own connection
                connections.connections.append(self) #adds self to list of other node's connections

            elif type(connections) is list: # if node is connected to multiple other nodes
                for currentConnection in connections:
                    if type(currentConnection) is node:
                        if currentConnection not in self.connections: # add current to list of connections if it isn't
                            # already in the list
                            self.connections.append(currentConnection)
                        if self not in currentConnection.connections: # add self to currentConnection's list of
                            # connections if it isn't already in the list
                            currentConnection.connections.append(self)
                    else:
                        raise TypeError('Only nodes can be connected to other nodes')

            else:
                raise TypeError('Only nodes can be connected to other nodes')

    def addConnection(self, connections):
        # Similar to initial connection adding but doesn't set up a new list
        if type(connections) is node:  # if node has one connection to another node
            if connections not in self.connections:
                self.connections.append(connections)  # adds listed node as own connection
            if self not in connections.connections:
                connections.connections.append(self)  # adds self to list of other node's connections

        elif type(connections) is list:  # if node is connected to multiple other nodes
            for currentConnection in connections:
                if type(currentConnection) is node:
                    if currentConnection not in self.connections:  # add current to list of connections if it isn't
                        # already in the list
                        self.connections.append(currentConnection)
                    if self not in currentConnection.connections:  # add self to currentConnection's list of
                        # connections if it isn't already in the list
                        currentConnection.connections.append(self)
                else:
                    raise TypeError('Only nodes can be connected to other nodes')

        else:
            raise TypeError('Only nodes can be connected to other nodes')

    def showConnections(self):
        if len(self.connections) == 0:
            return 'No connections'
        else:
            out = 'Connections: '
            for currentConnection in self.connections:
                out += str(currentConnection) + ', ' # add connection and setup for next connection to output string
            out = out[:-2] # cut off last comma space (', ')
            return out

    def isConnected(self, otherNode):
        return otherNode in self.connections # checks if otherNode is directly connected to current node

    def inGraph(self, otherNode):
        if otherNode in self.connections: # checks if node is connected to current node
            return True
        else:
            try:
                for connection in self.connections:
                    return connection.inGraph(otherNode)
            except:
                return False


    def __str__(self):
        return str(self.value)


x = node(1)
y = node(2,x) # connected to x
z = node(3,y) # connected to y
i = node(4,y) # connected to y
k = node(5) # connected to nothing

