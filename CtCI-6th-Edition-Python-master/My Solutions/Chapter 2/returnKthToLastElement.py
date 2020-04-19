from LinkedList import LinkedList
"""
Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list. 
"""

def returnKtoLast(linkedList, k):
    nodeNum = 0  # keeps track of what index we're on in the linked list
    for node in linkedList:
        nodeNum += 1  # increasing before check makes k = 0 the last element, the same way indexing works forwards
        if nodeNum == (len(linkedList) - k):  # len - k will be k elements back, so if index matches that, return value
            return node.value

    raise ValueError("There are not enough linked list nodes to go back that far")


ll = LinkedList()
ll.generate(10, 0, 9)
x = returnKtoLast(ll, 9)
