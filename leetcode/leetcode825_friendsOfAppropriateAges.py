# -*- coding: utf-8 -*-
"""
Some people will make friend requests. The list of their ages is given and ages[i] is the age of the ith person. 
Person A will NOT friend request person B (B != A) if any of the following conditions are true:
    age[B] <= 0.5 * age[A] + 7
    age[B] > age[A]
    age[B] > 100 && age[A] < 100
Otherwise, A will friend request B.
Note that if A requests B, B does not necessarily request A.  Also, people will not friend request themselves.
How many total friend requests are made?
"""
def numFriendRequests(ages):
    friendRequestCount = 0
    for personA in ages:
        ages.remove(personA) #Take personA out so they don't become friends with themselves
        for personB in ages: #Go through the list again to compare to the rest of the people in it
            if (personB <= ((.5 * personA)+7) or (personB > personA) or ((personB > 100) and (personA < 100))):
                #conditions given by problem for not friends
                friendRequestCount = friendRequestCount #do nothing
            else:
                friendRequestCount += 1 #friend request sent
        ages.insert(0,personA) #add person back into the list 
    return(friendRequestCount)
            
import random
ages = []
ageLength = random.randint(1,20000)
for x in range(ageLength+1):
    ages.append(random.randint(1,120))
#ages = [20,30,100,110,120]
print(numFriendRequests(ages))
"""
Example 1:
Input: [16,16]
Output: 2
Explanation: 2 people friend request each other.

Example 2:
Input: [16,17,18]
Output: 2
Explanation: Friend requests are made 17 -> 16, 18 -> 17.

Example 3:
Input: [20,30,100,110,120]
Output: 3
Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100. 

Notes:
    1 <= ages.length <= 20000.
    1 <= ages[i] <= 120.
"""