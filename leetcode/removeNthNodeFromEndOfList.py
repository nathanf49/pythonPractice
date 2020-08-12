class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    if type(head) is list:
        head = makeLinkedList(head) # allows the input of head to be a list instead of a linked list
    if head is None:
        return head

    # get one pointer n positions behind the other, when checker gets to the end, trailer will remove the node n
    # positions back
    checker = head
    trailer = head
    checkerIndex = 0
    while checker.next is not None:
        checkerIndex += 1
        checker = checker.next
        if checkerIndex > n: # the trailer moves forward when it is n positions behind the checker
            trailer = trailer.next

    if checkerIndex >= n:
        # when checker reaches the end, trailer will be n behind
        trailer.next = trailer.next.next
    else: # if the first node needs to be removed, n won't hit the checker index we're looking for
        head = head.next

    return head

    '''
    #Works fine here but leetcode won't run it
    removalIndex = listLength + 1 - n

    listIndex = 0
    checker = head
    while checker.next is not None: # runs a point through the linked list until finding the node that should be deleted
        listIndex += 1
        if listIndex == removalIndex:
            checker.next = checker.next.next
            break
        checker = checker.next

    return head


    
    # Works fine here but leetcode won't run it 
    
    # get all node values in order in a list
    values = []
    while head.next is not None:
        values.append(head.val)
        head = head.next
    values.append(head.val)

    values = values[:len(values)-n] + values[len(values)-n+1:] #remove the value n elements from the end

    # rebuild list
    listEnd = None
    for val in values:
        currentNode = ListNode(val)
        if listEnd is None:  # must be head if there is no end to linked ilst
            head = currentNode
        else:  # have to set this node as the next after previous
            listEnd.next = currentNode  # most recently added node is now at the end must be added after current end
        listEnd = currentNode  # current node is now at the end of the linked list

    return head
    '''

def makeLinkedList(values: list) -> ListNode: # makes a list into a linked list
    tail = None
    for currentVal in values:
        currentNode = ListNode(currentVal) # makes a node
        if tail is None: # this node will be the head of the linked list
            head = currentNode
        else: # this node will go after the current tail
            tail.next = currentNode
        tail = currentNode # this node will be the new tail
    return head

test = [1,2]
"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:

Given n will always be valid.
"""
