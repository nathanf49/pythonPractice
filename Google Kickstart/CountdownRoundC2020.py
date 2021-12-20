def main():
    testCases = int(input())
    c = 1
    while c <= testCases:
        countdown = input().split()
        countdown = int(countdown[1]) #how much we have to countdown
        seeker = '' # seeks countdowns
        for x in range(1,countdown+1):
            seeker = str(x) + ' ' + seeker # makes string of text we're searching for
        seeker = seeker[:-1] # cuts off last space
        text = input() # actual text to search through

        print('Case #' + str(c) + ': ' + str(text.count(seeker))) #output goes in str() function
        c+=1 # increment c to move onto the next test case

def main1():
    testCases = int(input())
    c = 1
    while c <= testCases:
        countdown = input().split()
        countdown = int(countdown[1])  # how much we have to countdown
        text = input()
        text = text.split()
        k = 0 # count for case
        text = [int(i) for i in text]
        for i in range(len(text)):
            if text[i] == countdown: # checks if integer at each index matches where countdown starts
                k += counting(text,i,countdown) # adds counting to k, counting returns a 1 if it works, 0 if not

        print('Case #' + str(c) + ': ' + str(k))
        c += 1

def counting(text,i,c): # input text, index, # to coundown from
    try:
        if (text[i] == 1) and (c == 1): #case counts down to 1
            return 1
        elif text[i] == c: # continue case
            return counting(text,i+1,c-1)
        else: # case doesn't count down
            return 0
    except:
        return 0


if __name__ == '__main__':
    main1()
"""
Problem

Avery has an array of N positive integers. The i-th integer of the array is Ai.

A contiguous subarray is an m-countdown if it is of length m and contains the integers m, m-1, m-2, ..., 2, 1 in that order. For example, [3, 2, 1] is a 3-countdown.

Can you help Avery count the number of K-countdowns in her array?
Input

The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a line 
containing the integers N and K. The second line contains N integers. The i-th integer is Ai.

Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the number of K-countdowns in her array.
Limits

Time limit: 20 seconds.
Memory limit: 1 GB.
1 ≤ T ≤ 100.
2 ≤ K ≤ N.
1 ≤ Ai ≤ 2 × 105, for all i.
Test Set 1

2 ≤ N ≤ 1000.
Test Set 2

2 ≤ N ≤ 2 × 105 for at most 10 test cases.
For the remaining cases, 2 ≤ N ≤ 1000.
Sample
Sample Input
save_alt
content_copy

3
12 3
1 2 3 7 9 3 2 1 8 3 2 1
4 2
101 100 99 98
9 6
100 7 6 5 4 3 2 1 100

Sample Output
save_alt
content_copy

Case #1: 2
Case #2: 0
Case #3: 1

In sample case #1, there are two 3-countdowns as highlighted below.

    1 2 3 7 9 3 2 1 8 3 2 1
    1 2 3 7 9 3 2 1 8 3 2 1

In sample case #2, there are no 2-countdowns.

In sample case #3, there is one 6-countdown as highlighted below.

    100 7 6 5 4 3 2 1 100

"""