def mergeSort(L):
    """
    Merge sort works recursively. It breaks the list into smaller lists until it has each list of length 1. Then it
    compares the smallest value from 1 list to the smallest value of another list, inserting the smallest value each
    time until 1 list is entirely added to the new list. Then you know the other list is already sorted, so you can just
    add the rest of that list onto your new list and keep building until you have the entire list sorted.

    Merge sort is faster than selection sort and bubble sort, but requires more space as
    Worst Case: O(nlog(n))
    """
    if len(L) < 2: #base case, already sorted if there is only 1 element
        return L.copy()
    middle = len(L) // 2
    left = mergeSort(L[:middle]) #recursively calls mergeSort on left and right until it reaches base case
    right = mergeSort(L[middle:])
    return merge(left,right)

def merge(left,right):
    """
    helper function that does the work for merge sort
    """
    print('Left:', left)
    print('Right:', right)
    result = [] #creates the new list that the sublists will sort into
    i,j = 0,0
    while i < len(left) and j < len(right): #runs until either subsection reaches the end
        if left[i] < right[j]: #appends min of 2 sublists to the new list
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left): #one of these sublists will not run because the loop above breaks when either reaches the same
        # conditions here, the other sublist will append the rest of the list since it is already sorted
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def selectionSort(L):
    """
    Selection sort goes through a list comparing to find the smallest element in the unsorted list.
    That element is then put at the start of the list as it is the smallest element. The next element
    is found by doing the same thing, but skipping the first element as it is already sorted. Then 2
    elements are skipped for the 3rd loop and so on.

    Worst case: O(n^2), not very efficient but generally faster than bubble sort as first i elements are guaranteed to
    be in place
    """
    for i in range(len(L) - 1):
        # print(L) #shows the sort as each element is put in place
        minIndex = i  # default for minIndex/Val is the first thing in the unsorted part
        minVal = L[i]
        j = i + 1
        while j < len(L):
            if L[j] < minVal:  # saves smallest value found
                minIndex = j
                minVal = L[j]
            j += 1
        temp = L[i]  # swaps the smallest element from the unsorted part to the start of the unsorted part/end of the
        # sorted part
        L[i] = L[minIndex]
        L[minIndex] = temp
    return L


def bubbleSort(L):
    """
    Repeatedly steps through the list comparing adjacent elements if they are in the wrong order
    Worst case: O(n^2)
    """
    isSorted = False
    while not isSorted:
        # print(L)
        isSorted = True  # assume list is sorted until a comparison shows an element is out of order, then set isSorted
        # to False to make the loop check the list again
        for j in range(1, len(L)):
            if L[j - 1] > L[j]:  # if an element has a greater element after it, they need to be swapped to get the list
                # in order
                isSorted = False
                temp = L[j]
                L[j] = L[j - 1]
                L[j - 1] = temp
    return L

import random
def randomList(n,MAX):
    L = []
    for x in range(n):
        L.append(random.randint(0,MAX))
    return L
