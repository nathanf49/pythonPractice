from LinkedList import LinkedList

"""
Remove Dups: Write code to remove duplicates from an unsorted linked list. 
"""


def removeDuplicates(linkedList):
    if linkedList.head is None:
        return linkedList
    current = linkedList.head
    values = [current.value]  # list of values seen so far
    while current.next is not None:
        if current.next.value not in values:  # if the value has not been seen yet, add it to the list of values
            values.append(current.next.value)
            current = current.next  # move to next node
        else:
            current.next = current.next.next  # remove node if the value has been seen

    return linkedList


"""
FOLLOW UP How would you solve this problem if a temporary buffer is not allowed?
"""


def removeDuplicatesFollowUp(linkedList):
    if linkedList.head is None:
        return linkedList

    for node in linkedList: # goes through nodes
        current = node # checker node
        while current.next is not None: # checker runs through remaining nodes in list
            if current.next.value == node.value: # if checker node matches original node value, remove it
                current.next = current.next.next
            else:
                current = current.next
    return linkedList


ll = LinkedList()
ll.generate(100, 0, 9)

blank = LinkedList()
blank.generate(0, 0, 9)
