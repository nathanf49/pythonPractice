MaxNumOfCases = int(input())
CaseNum = 1 # starting case number

while CaseNum <= MaxNumOfCases:
    i = input()
    i = i.split()
    budget = int(i[1]) # budget for case
    houses = input() # takes houses as an input
    houses = houses.split()
    houses = [int(i) for i in houses] # converts houses to list of numbers
    houses.sort() # sorts houses by price
    housesBought = 0
    while budget - houses[0] >= 0:
        budget -= houses[0] # purchases cheapest house
        housesBought += 1 # keeps tracks of houses bought
        houses = houses[1:] # gets rid of cheapest house as being available

    print('Case #' + str(CaseNum) + ': ' + str(housesBought))
    CaseNum += 1 # ends program by putting CaseNum higher than MaxNumOfCases

"""
Problem

There are N houses for sale. The i-th house costs Ai dollars to buy. You have a budget of B dollars to spend.
What is the maximum number of houses you can buy?


Input

The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a single
line containing the two integers N and B. The second line contains N integers. The i-th integer is Ai, the cost of the i-th house.


Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is
the maximum number of houses you can buy.


Limits

Time limit: 15 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
1 ≤ B ≤ 105.
1 ≤ Ai ≤ 1000, for all i.
Test set 1

1 ≤ N ≤ 100.
Test set 2

1 ≤ N ≤ 105.
Sample

Input

3
4 100
20 90 40 90
4 50
30 30 10 10
3 300
999 999 999



Output

Case #1: 2
Case #2: 3
Case #3: 0



In Sample Case #1, you have a budget of 100 dollars. You can buy the 1st and 3rd houses for 20 + 40 = 60 dollars.
In Sample Case #2, you have a budget of 50 dollars. You can buy the 1st, 3rd and 4th houses for 30 + 10 + 10 = 50 dollars.
In Sample Case #3, you have a budget of 300 dollars. You cannot buy any houses (so the answer is 0).

Note: Unlike previous editions, in Kick Start 2020, all test sets are visible verdict test sets, meaning you receive instant feedback upon submission.



Analysis

We want to buy as many as possible houses. Intuitively, we can keep buying the cheapest house. The rationale is to save money at each step so we could buy more in the end. One way to implement this strategy is to sort all the houses by prices from low to high and then buy houses one by one until we run out of money.

The sorting part has O(N log N) time complexity and the processing part has O(N) time complexity. Using counting sort could reduce the sorting complexity to O(N) since the range of the prices is [1, 1000]. The overall time complexity is O(N).

Let's prove the correctness of this greedy algorithm. Let the solution produced by the greedy algorithm be A = {a1, a2, ..., ak} and an optimal solution O = {o1, o2, ..., om}.

If O and A are the same, we are done with the proof. Let's assume that there is at least one element oj in O that is not present in A. Because we always take the smallest element from the original set, we know that any element that is not in A is greater than or equal to any ai in A. We could replace oj with the absent element in A without worsening the solution, because there will always be element in A that is not in O. We then increased number of elements in common between A and O, hence we can repeat this operation only finite number of times. We could repeat this process until all the elements in O are elements in A. Therefore, A is as good as any optimal solution.

"""
