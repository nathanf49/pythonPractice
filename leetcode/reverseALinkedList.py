def reverseList(head: ListNode):
    if head is None:
        return head

    if type(head) is None:
        return head
    # start by getting all the values in a regular list (easier to reverse)
    values = []
    while head.next is not None:
        values.append(head.val)
        head = head.next
    values.append(head.val)  # above loop misses last value since it will have next as None

    # go through values in reverse and make a new linked list

    listEnd = None
    for val in values[::-1]:
        currentNode = ListNode(val)
        if listEnd is None:  # must be head if there is no end to linked ilst
            head = currentNode
        else:  # have to set this node as the next after previous
            listEnd.next = currentNode  # most recently added node is now at the end must be added after current end
        listEnd = currentNode  # current node is now at the end of the linked list

    return head
"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""