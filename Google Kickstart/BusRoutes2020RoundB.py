def main():
    maxCases = int(input())
    c = 1  # case num
    while c <= maxCases:
        c += 1  # increments case
        i = input()
        i = i.split()
        N = int(i[0])
        maxDay = int(i[1])  # saves second part of input as max day
        bus = input()
        bus = bus.split()
        bus = [int(i) for i in bus]  # saves bus schedule as list of ints
        if N != len(bus):
            raise Exception('N should be equal to the number of busses')
        for x in range(len(bus)):
            m = 2
            bus[x] = [bus[x]]
            while bus[x][-1] <= maxDay - bus[x][0]:  # makes a full schedule up to max day for each bus
                bus[x].append(bus[x][0] * m)
                m += 1
            bus[x].reverse()
            #print(bus[x])

        leaving = bus[-1][0]  # finds last day last bus is leaving
        if leaving > maxDay:
            leaving = bus[-1][1]  # ensures multiple didn't go over max day

        for x in reversed(range(0, N-1)):  # goes through busses all busses except the last in reverse order
            day = 0
            print(x)
            while bus[x][day] > leaving:  # goes through days in backwards until leaving day is equal or less than current bus
                day += 1
                print(bus[x][day])
            leaving = bus[x][day]


        print('Case #' + str(c - 1) + ': ' + str(leaving))


if __name__ == '__main__':
    main()

    # Save fastest path and show (max days - fastest path)?

"""
Sample

Input
 

3
3 10
3 7 2
4 100
11 10 5 50
1 1
1

  
Output
	

Case #1: 6
Case #2: 99
Case #3: 1


Input

The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a line containing the two integers N and D. Then, another line follows containing N integers, the i-th one is Xi.
Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the latest day she could take the first bus, and still finish her journey by day D.
Limits

Time limit: 10 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
1 ≤ Xi ≤ D.
1 ≤ N ≤ 1000.
It is guaranteed that it is possible for Bucket to finish her journey by day D.
Test set 1

1 ≤ D ≤ 100.
Test set 2

1 ≤ D ≤ 1012.

  

In Sample Case #1, there are N = 3 bus routes and Bucket must arrive by day D = 10. She could:

    Take the 1st bus on day 6 (X1 = 3),
    Take the 2nd bus on day 7 (X2 = 7) and
    Take the 3rd bus on day 8 (X3 = 2).

In Sample Case #2, there are N = 4 bus routes and Bucket must arrive by day D = 100. She could:

    Take the 1st bus on day 99 (X1 = 11),
    Take the 2nd bus on day 100 (X2 = 10),
    Take the 3rd bus on day 100 (X3 = 5) and
    Take the 4th bus on day 100 (X4 = 50),

In Sample Case #3, there is N = 1 bus route and Bucket must arrive by day D = 1. She could:

    Take the 1st bus on day 1 (X1 = 1).

"""
