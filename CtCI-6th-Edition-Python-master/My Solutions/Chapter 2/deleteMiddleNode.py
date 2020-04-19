from LinkedList import LinkedList
"""
Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, 
not necessarily the exact middle) of a singly linked list, given only access to that node. EXAMPLE Input: the node c 
from the linked list a - >b- >c - >d - >e- >f Result: nothing is returned, but the new linked list looks like 
a->b->d->e->f 
"""

def deleteMiddleNode(linkedList):
    if len(linkedList) < 3: # never touch head or tail
        raise ValueError("List must have more than 2 nodes to delete the middle node")
    listMiddle = round((len(linkedList) / 2) - 0.9) # finds index of middle of linked list, always deletes lower element
    # instead of rounding up
    nodeNum = 0  # keeps track of index
    for node in linkedList:
        if (nodeNum + 1) == listMiddle:  # if the index of the next node would be the middle, remove it and return new
            # list
            node.next = node.next.next
            break # function does not return anything, list is modified in place
        nodeNum += 1  # otherwise, increase index and continue loop


ll = LinkedList()
ll.generate(5,0,9)
print(ll)
deleteMiddleNode(ll)
print(ll)
deleteMiddleNode(ll)
print(ll)
deleteMiddleNode(ll)
print(ll)
# deleteMiddleNode(ll) # throws value error, 2 elements 