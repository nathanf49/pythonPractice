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

    def atEnd(self,newData):
        newNode = node(newData) #creates node
        if self.head is None: #if the list is blank
            self.head = newNode #puts newNode at the head of list
        else: #if list exists, must find the end
            place = self.head
            while place.next is not None: #while not at the end
                place = place.next #points to next node in list
            place.next = newNode #inserts node

    def traverse(self): #for printing linked list values in order
        node = self.head
        print(node) #prints first node
        while node != None: #while not at end of linked list
            print(node.data) #prints data value
            node = node.next #moves to next node

list = singlyLinkedList()
a = node(2)
list.head = a
a.next = node(3)
list.atBeginning(1)
list.atEnd(4)
list.traverse()
