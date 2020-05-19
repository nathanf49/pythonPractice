from LinkedList import LinkedList
"""
Intersection; Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. 
Note that the intersection is defined based on reference, not value. That is, if the kth node of the first linked list 
is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting.
"""

def intersection(linkedList1, linkedList2):
    if len(linkedList1) <= len(linkedList2):  # checks which list is shorter to maximize efficiency
        for node in linkedList1:
            if node in linkedList2:  # in checks by node reference, not value
                return True
        return False

    else:
        for node in linkedList2:
            if node in linkedList1:
                return True
        return False

listA = LinkedList()
listA.add(5)
listB = listA
listA.add(7)
listB.add(7)
listA.add(15)
listB.add('hi')
listC = LinkedList()
listC.generate(10,0,9)

print(intersection(listA, listB)) # should be true since listB is listA
print(intersection(listA,listC)) # should be false no matter what is in listC since references will be different