# -*- coding: utf-8 -*-
"""
We have an array A of integers, and an array queries of queries.
For the i-th query val = queries[i][0], index = queries[i][1], we add val to A[index].  
Then, the answer to the i-th query is the sum of the even values of A.
(Here, the given index = queries[i][1] is a 0-based index, and each query permanently modifies the array A.)
Return the answer to all queries.  Your answer array should have answer[i] as the answer to the i-th query.
"""
def sumEvenAfterQueries(A, queries):
    evenCount = [] #list of sum of evens after each pass through
    for query in queries: #for each query
        evenSum = 0
        A[query[1]] += query[0] #add first part of current query to index of A denoted by second part of current query
        for element in A: 
            if A[query[1]] % 2 == 0: #checks for even numbers
                evenSum += element #keeps track of sum of even numbers
        evenCount.append(evenSum)
    return(evenCount)
    
import random
maximum = 10000
Alength = random.randint(1,maximum)
A = []
for x in range(Alength):
    A.append(random.randint(-maximum,maximum))
queryLength = random.randint(1,maximum)
queries = []
for x in range(queryLength):
    queries.append([random.randint(-maximum,maximum), random.randint(0,Alength-1)])
print(sumEvenAfterQueries(A, queries))
"""
Example 1:
Input: A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
Output: [8,6,2,4]
Explanation: 
At the beginning, the array is [1,2,3,4].
After adding 1 to A[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
After adding -3 to A[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
After adding -4 to A[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
After adding 2 to A[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.
Note:
    1 <= A.length <= 10000
    -10000 <= A[i] <= 10000
    1 <= queries.length <= 10000
    -10000 <= queries[i][0] <= 10000
    0 <= queries[i][1] < A.length
"""