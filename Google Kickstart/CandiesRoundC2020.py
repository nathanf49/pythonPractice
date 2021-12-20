def main():
    tests = int(input())
    t = 1
    while t <= tests:
        n = input().split() # number of inputs and operations
        n = int(n[1])
        q = input().split() # array of text
        q = [int(i) for i in q]
        sweetness = []

        while n > 0:
            i = input().split()
            if i[0] == 'U': # update
                q[int(i[1]) - 1] = int(i[2]) # updates q

            elif i[0] =='Q':# query
                l = int(i[1]) - 1
                r = int(i[2]) - 1
                s = 0
                operation = '+' # operation switches with each operation
                operator = 1 # how much we multiply by (increases by 1 with each operation)
                for x in range(l,r+1): # x is index
                    if operation == '-':
                        s -= q[x] * operator
                        operation = '+' # switch to + for next operation
                    elif operation == '+':
                        s += q[x] * operator
                        operation = '-' # switch to - for next operation
                    operator += 1
                sweetness.append(s) # keeps a list of all sweetness scores to takes the sum of
            n -= 1

        print('Case #' + str(t) + ': ' + str(sum(sweetness)))
        t += 1

if __name__ == '__main__':
    main()
"""
 Carl has an array of N candies. The i-th element of the array (indexed starting from 1) is Ai representing sweetness value of the i-th candy. He would like to perform a series of Q operations. There are two types of operation:

    Update the sweetness value of a candy in the array.
    Query the sweetness score of a subarray.

The sweetness score of a subarray from index l to r is: Al × 1 - Al+1 × 2 + Al+2 × 3 - Al+3 × 4 + Al+4 × 5 ...

More formally, the sweetness score is the sum of (-1)i-lAi × (i - l + 1), for all i from l to r inclusive.

For example, the sweetness score of:

    [3, 1, 6] is 3 × 1 - 1 × 2 + 6 × 3 = 19
    [40, 30, 20, 10] is 40 × 1 - 30 × 2 + 20 × 3 - 10 × 4 = 0
    [2, 100] is 2 × 1 - 100 × 2 = -198

Carl is interested in finding out the total sum of sweetness scores of all queries. If there is no query operation, the sum is considered to be 0. Can you help Carl find the sum?
Input

The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a line containing N and Q. The second line contains N integers describing the array. The i-th integer is Ai. The j-th of the following Q lines describe the j-th operation. Each line begins with a single character describing the type of operation (U for update, Q for query).

    For an update operation, two integers Xj and Vj follow, indicating that the Xj-th element of the array is changed to Vj.
    For a query operation, two integers Lj and Rj follow, querying the sweetness score of the subarray from the Lj-th element to the Rj-th element (inclusive).

Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the total sum of sweetness scores of all the queries.
Limits

Time limit: 20 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
1 ≤ Ai ≤ 100, for all i.
1 ≤ N ≤ 2 × 105 and 1 ≤ Q ≤ 105 for at most 6 test cases.
For the remaining cases, 1 ≤ N ≤ 300 and 1 ≤ Q ≤ 300.
If the j-th operation is an update operation, 1 ≤ Xj ≤ N and 1 ≤ Vj ≤ 100.
If the j-th operation is a query operation, 1 ≤ Lj ≤ Rj ≤ N.
Test set 1

There will be at most 5 update operations.
Test set 2

There are no special constraints.
Sample

Input


2
5 4
1 3 9 8 2
Q 2 4
Q 5 5
U 2 10
Q 1 2
3 3
4 5 5
U 1 2
U 1 7
Q 1 2

Output

Case #1: -8
Case #2: -3



In sample case #1:

    The first query asks for the sweetness score of [3, 9, 8] which is 3 × 1 - 9 × 2 + 8 × 3 = 9.
    The second query asks for the sweetness score of [2] which is 2 × 1 = 2.
    The third query asks for the sweetness score of [1, 10] which is 1 × 1 - 10 × 2 = -19.

Thus, the final output should be 9 + 2 - 19 = -8.

In sample case #2:

    The first and only query asks for the sweetness score of [7, 5] which is 7 × 1 - 5 × 2 = -3.

Thus, the final output should be -3.
"""