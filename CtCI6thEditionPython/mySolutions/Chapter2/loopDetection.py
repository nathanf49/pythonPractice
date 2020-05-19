from LinkedList import LinkedList

"""
Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop. 
DEFINITION Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, 
so as to make a loop in the linked list. 
EXAMPLE Input: A->8->C->D->E-> C [the same C as earlier] Output: C
"""

def loopDetection(linkedList):
    currentNode = linkedList.head
    nodesSeen = []  # list of nodes already seen
    while currentNode not in nodesSeen: # if a node we've already past appears, break and return it
        nodesSeen.append(currentNode) # add current node to list we've seen
        currentNode = currentNode.next # move to next node
    return currentNode

ll = LinkedList()
ll.generate(10,0,9) # generates 10 values between 0 and 9
ll.tail.next = ll.head # loops the end of the list back around to the head
loopNode = loopDetection(ll) # should return head node
print(ll)
print(loopNode)