maxCases = int(input()) # reads first line (max # of cases)

for case in range(1,maxCases+1): # runs for number of cases
    k = 0 # peak count
    numOfPeaks = int(input()) # takes input for how many peaks there are
    peaks = input() # takes input of as many spaced numbers as numOf Peaks
    peaks = peaks.split() # splits string into a list
    peaks = [int(i) for i in peaks] # changes strings to ints
    for peak in peaks: # goes through each peak
        i = peaks.index(peak) # gets index of current peak
        if i != 0 and i != numOfPeaks-1: # runs if i is not first or last peak (requirement of problem)
            if peak > peaks[i+1] and peak > peaks[i-1]: # is a peak if previous and next peak are smaller
                k += 1

    print("Case #" + str(case) + ": " + str(k)) # print peaks/case
    case += 1


"""
Problem

Li has planned a bike tour through the mountains of Switzerland. His tour consists of N checkpoints, numbered from 1 to N in the order he will visit them. The i-th checkpoint has a height of Hi.

A checkpoint is a peak if:

    It is not the 1st checkpoint or the N-th checkpoint, and
    The height of the checkpoint is strictly greater than the checkpoint immediately before it and the checkpoint immediately after it.

Please help Li find out the number of peaks.
Input

The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a line containing the integer N. The second line contains N integers. The i-th integer is Hi.
Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the number of peaks in Li's bike tour.
Limits

Time limit: 10 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
1 ≤ Hi ≤ 100.
Test set 1

3 ≤ N ≤ 5.
Test set 2

3 ≤ N ≤ 100.
Sample

Input
  	
Output
 

4
3
10 20 14
4
7 7 7 7
5
10 90 20 90 10
3
10 3 10

  

	

Case #1: 1
Case #2: 0
Case #3: 2
Case #4: 0

  

    In sample case #1, the 2nd checkpoint is a peak.
    In sample case #2, there are no peaks.
    In sample case #3, the 2nd and 4th checkpoint are peaks.
    In sample case #4, there are no peaks.
"""