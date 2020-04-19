from LinkedList import LinkedList


def palindrome(linkedList):
    valueList = llToList(linkedList)
    reversedList = valueList[:]  # makes copy of value list
    reversedList.reverse()  # reverses value list
    if valueList == reversedList:  # compares list of values to reversed list of values
        return True
    else:
        return False


def llToList(linkedList):
    """
    Makes a list of the values in a linked list
    """
    valueList = []
    for node in linkedList:
        valueList.append(node.value)
    return valueList


ll = LinkedList()
ll.add(1)
ll.add(0)
ll.add(1)
print(palindrome(ll))

test = LinkedList()
test.generate(3, 0, 2)
print(palindrome(test))
