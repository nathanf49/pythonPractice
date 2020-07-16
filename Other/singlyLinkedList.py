class node: #create node data structure, nodes will have data and point to next node
    def __init__(self, data): #takes in a data value
        self.data = data #read data value into Node
        self.next = None #default for Node is to have no next value to account for last value in list

class singlyLinkedList: #create linked list data structure to hold nodes
    def __init__(self):
        self.head = None #default is empty list

    def atBeginning(self,newData): #to insert node at start
        newNode = node(newData) #creates node
        newNode.next = self.head #points next value of new node to start of the list we have
        self.head = newNode #inserts node

    def insertAfter(self,newData,existingNode):
        if existingNode != None: #if the node exists
            newNode = node(newData) #creates node
            newNode.next = existingNode.next #moves node after existing node after the new node before existingNode.next is cleared
            existingNode.next = newNode #puts the new node in after the existingNode
        else:
            print('Node could not be found')

    def atEnd(self,newData):
        newNode = node(newData) #creates node
        if self.head is None: #if the list is blank
            self.head = newNode #puts newNode at the head of list
        else: #if list exists, must find the end
            place = self.head
            while place.next is not None: #while not at the end
                place = place.next #points to next node in list
            place.next = newNode #inserts node

    def positionialInsert(self,newData,position):
        if type(position) is not int: #checks that data type is int or can't count
            print('That is not a valid position')
            return
        else:
            newNode = node(newData)
            currentPosition = 0 #initializes position at 0 and place at head of list
            place = self.head
            while currentPosition != position:
                place = place.next #goes to next place and increments count until reaching expected location
                currentPosition += 1
            if currentPosition == position: #inserts new node
                place.next = newNode


    def removeNode(self,removeData):
        node = self.head #starts at head
        while node.next != removeData: #goes through list looking for removeData
            node = node.next
            if node.next is None: #says node could not be found if it reaches the end of the list
                print('Node could not be found')
                return
        if node.next == removeData: # if the data to remove is in the next node
            if node.next.next is not None: #if there is a node after the next node
                node.next = node.next.next #skips the node to be removed in the list
            else: #if the data to be removed is at the end of the singlyLinkedList
                node.next = None #sets next value to None, effectively ending list

    def traverse(self): #for printing linked list values in order
        node = self.head
        print(node) #prints first node
        while node != None: #while not at end of linked list
            print(node.data) #prints data value
            node = node.next #moves to next node

list = singlyLinkedList()
a = node(1)
list.head = a
b = node(3)
a.next = node(2)
a.next.next = b
list.atBeginning(0)
c = node(5)
list.atEnd(c)
d = node(4)
list.positionialInsert(4,4)
list.traverse()
