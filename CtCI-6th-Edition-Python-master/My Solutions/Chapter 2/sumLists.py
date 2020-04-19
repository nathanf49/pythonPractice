from LinkedList import LinkedList

"""
Sum Lists: You have two numbers represented by a linked list, where each node contains a single digit. The digits are
stored in reverse order, such that the Vs digit is at the head of the list. Write a function that adds the two numbers
and returns the sum as a linked list.
EXAMPLE Input: (7-> 1 -> 6) + (5 -> 9 -> 2). That is,617 + 295. Output: 2 -> 1 -> 9. That is, 912
"""


def sumListsReverse(linkedList1, linkedList2):
    num1 = linkedListToNumStr(linkedList1)
    num2 = linkedListToNumStr(linkedList2)
    total = str(int(num1[::-1]) + int(num2[::-1]))  # casts reversed strings of num1 and num2 as integers and adds them,
    # then converts back to string so each digit can be put into a new linked list
    newList = LinkedList()
    for char in total[::-1]:  # reverses total
        newList.add(int(char))  # puts each digit into new linked list
    return newList


def linkedListToNumStr(linkedList):
    """
    Returns a string of all digits in linked List
    """
    if len(linkedList) == 0: # don't want to return None or we'll get errors trying to cast/reverse/add
        return '0'
    numStr = ''
    for node in linkedList:
        numStr += str(node.value)
    return numStr


"""
FOLLOW UP Suppose the digits are stored in forward order. Repeat the above problem. 
EXAMPLE Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).That is, 617 + 295, Output:9 -> 1 -> 2,That is,912
"""

def sumListsForward(linkedList1, linkedList2):
    num1 = linkedListToNumStr(linkedList1)
    num2 = linkedListToNumStr(linkedList2)
    total = str(int(num1) + int(num2))  # casts strings of num1 and num2 as integers and adds them,
    # then converts back to string so each digit can be put into a new linked list
    newList = LinkedList()
    for char in total:
        newList.add(int(char))  # puts each digit into new linked list
    return newList


ll1 = LinkedList()
ll1.generate(3,0,9)
ll2 = LinkedList()
ll2.generate(3,0,9)
x = sumListsReverse(ll1,ll2)
y = sumListsForward(ll1, ll2)