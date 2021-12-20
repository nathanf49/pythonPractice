def main():
    tests = int(input())
    t = 1
    while t <= tests:
        dayCount = int(input())  # how many days will be in array
        days = input().split()
        days = [int(i) for i in days]  # read array for visitors on each day
        recordBreakingDays = 0
        for x in range(dayCount):
            pastDays = days[0:x]
            if x != 0:  # Check is visitors is greater than past days
                if days[x] > max(pastDays):
                    maxFlag = True
                else:  # if x is not greater than other days
                    maxFlag = False
            else:  # assume day[x] is greater than past days if there are no past days
                maxFlag = True
            if maxFlag == True:
                if x == dayCount - 1:  # x is the last day
                    recordBreakingDays += 1
                else:
                    if days[x] > days[x + 1]:  # number of visitors on day is larger than visitors the following day
                        recordBreakingDays += 1

        print('Case #' + str(t) + ': ' + str(recordBreakingDays))
        t += 1


if __name__ == '__main__':
    main()

"""
 Isyana is given the number of visitors at her local theme park on N consecutive days. The number of visitors on the i-th day is Vi. A day is record breaking if it satisfies both of the following conditions:

    The number of visitors on the day is strictly larger than the number of visitors on each of the previous days.
    Either it is the last day, or the number of visitors on the day is strictly larger than the number of visitors on the following day.

Note that the very first day could be a record breaking day!

Please help Isyana find out the number of record breaking days.
Input

The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a line containing the integer N. The second line contains N integers. The i-th integer is Vi.
Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the number of record breaking days.
Limits

Time limit: 20 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
0 ≤ Vi ≤ 2 × 105.
Test set 1

1 ≤ N ≤ 1000.
Test set 2

1 ≤ N ≤ 2 × 105 for at most 10 test cases.
For the remaining cases, 1 ≤ N ≤ 1000.
Sample

Input
4
8
1 2 0 7 2 0 2 0
6
4 8 15 16 23 42
9
3 1 4 1 5 9 2 6 5
6
9 9 9 9 9 9

Output
Case #1: 2
Case #2: 1
Case #3: 3
Case #4: 0

  

In Sample Case #1, the bold and underlined numbers in the following represent the record breaking days: 1 2 0 7 2 0 2 0.

In Sample Case #2, only the last day is a record breaking day.

In Sample Case #3, the first, the third, and the sixth days are record breaking days. 
"""