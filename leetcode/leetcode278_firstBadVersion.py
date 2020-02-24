"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of
your product fails the quality check. Since each version is developed based on the previous version, all the versions
after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following
ones to be bad.
You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find
the first bad version. You should minimize the number of calls to the API.
"""
def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    minTrue = n  # keeps track of the lowest bad version found so far
    maxFalse = 0
    while isBadVersion(maxFalse+1) is False:
        if isBadVersion(int((minTrue+maxFalse)/2)) is True:
            minTrue = int((minTrue+maxFalse)/2)
        else:
            maxFalse = int((minTrue+maxFalse)/2)
    return maxFalse+1

def isBadVersion(versionNum):
    if versionList[versionNum] == 1:
        return True
    else:
        return False

import random
length = 1000
versionList = [0] * length
for x in range(random.randint(1,length-1),length):
    versionList[x] = 1
print("Answer: ", versionList.index(1))
print(firstBadVersion(length))
"""
Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 
"""