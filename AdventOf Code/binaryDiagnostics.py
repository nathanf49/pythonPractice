import numpy as np

def diagnosticReport(reports):
    bit1_0 = 0 # keeps count of how many lines have 1 or 0
    bit1_1 = 0
    bit2_1 = 0
    bit2_0 = 0
    bit3_0 = 0
    bit3_1 = 0
    bit4_0 = 0
    bit4_1 = 0
    bit5_0 = 0
    bit5_1 = 0
    bit6_1 = 0
    bit6_0 = 0
    bit7_0 = 0
    bit7_1 = 0
    bit8_0 = 0
    bit8_1 = 0
    bit9_0 = 0
    bit9_1 = 0
    bit10_0 = 0
    bit10_1 = 0
    bit11_0 = 0
    bit11_1 = 0
    bit12_0 = 0
    bit12_1 = 0
    for line in reports:
        if line[0] == '0':
            bit1_0 += 1
        else:
            bit1_1 += 1
        if line[1] == '0':
            bit2_0 += 1
        else:
            bit2_1 += 1
        if line[2] == '0':
            bit3_0 += 1
        else:
            bit3_1 += 1
        if line[3] == '0':
            bit4_0 += 1
        else:
            bit4_1 += 1
        if line[4] == '0':
            bit5_0 += 1
        else:
            bit5_1 += 1
        if line[5] == '0':
            bit6_0 += 1
        else:
            bit6_1 += 1
        if line[6] == '0':
            bit7_0 += 1
        else:
            bit7_1 += 1
        if line[7] == '0':
            bit8_0 += 1
        else:
            bit8_1 += 1
        if line[8] == '0':
            bit9_0 += 1
        else:
            bit9_1 += 1
        if line[9] == '0':
            bit10_0 += 1
        else:
            bit10_1 += 1
        if line[10] == '0':
            bit11_0 += 1
        else:
            bit11_1 += 1
        if line[11] == '0':
            bit12_0 += 1
        else:
            bit12_1 += 1
    gamma = ''
    epsilon = ''
    if bit1_0 > bit1_1:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'
    if bit2_0 > bit2_1:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'
    if bit3_0 > bit3_1:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'
    if bit4_0 > bit4_1:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'
    if bit5_0 > bit5_1:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'
    if bit6_0 > bit6_1:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'
    if bit7_0 > bit7_1:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'
    if bit8_0 > bit8_1:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'
    if bit9_0 > bit9_1:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'
    if bit10_0 > bit10_1:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'
    if bit11_0 > bit11_1:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'
    if bit12_0 > bit12_1:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

    gamma = int(gamma,2)
    epsilon = int(epsilon,2)

    print(gamma * epsilon)

def diagnosticReport2(reports):
    bit1_0 = 0 # keeps count of how many lines have 1 or 0
    bit1_1 = 0
    bit2_1 = 0
    bit2_0 = 0
    bit3_0 = 0
    bit3_1 = 0
    bit4_0 = 0
    bit4_1 = 0
    bit5_0 = 0
    bit5_1 = 0
    bit6_1 = 0
    bit6_0 = 0
    bit7_0 = 0
    bit7_1 = 0
    bit8_0 = 0
    bit8_1 = 0
    bit9_0 = 0
    bit9_1 = 0
    bit10_0 = 0
    bit10_1 = 0
    bit11_0 = 0
    bit11_1 = 0
    bit12_0 = 0
    bit12_1 = 0
    for line in reports:
        if line[0] == '0':
            bit1_0 += 1
        else:
            bit1_1 += 1
        if line[1] == '0':
            bit2_0 += 1
        else:
            bit2_1 += 1
        if line[2] == '0':
            bit3_0 += 1
        else:
            bit3_1 += 1
        if line[3] == '0':
            bit4_0 += 1
        else:
            bit4_1 += 1
        if line[4] == '0':
            bit5_0 += 1
        else:
            bit5_1 += 1
        if line[5] == '0':
            bit6_0 += 1
        else:
            bit6_1 += 1
        if line[6] == '0':
            bit7_0 += 1
        else:
            bit7_1 += 1
        if line[7] == '0':
            bit8_0 += 1
        else:
            bit8_1 += 1
        if line[8] == '0':
            bit9_0 += 1
        else:
            bit9_1 += 1
        if line[9] == '0':
            bit10_0 += 1
        else:
            bit10_1 += 1
        if line[10] == '0':
            bit11_0 += 1
        else:
            bit11_1 += 1
        if line[11] == '0':
            bit12_0 += 1
        else:
            bit12_1 += 1

    oxygen = '' # most common number from each position, should be 1 if equally common, this is oxygen rating
    CO2 = '' # least common number from each position, this is CO2 rating
    if bit1_0 > bit1_1:
        oxygen += '0'
        CO2 += '1'
    else:
        oxygen += '1'
        CO2 += '0'
    if bit2_0 > bit2_1:
        oxygen += '0'
        CO2 += '1'
    else:
        oxygen += '1'
        CO2 += '0'
    if bit3_0 > bit3_1:
        oxygen += '0'
        CO2 += '1'
    else:
        oxygen += '1'
        CO2 += '0'
    if bit4_0 > bit4_1:
        oxygen += '0'
        CO2 += '1'
    else:
        oxygen += '1'
        CO2 += '0'
    if bit5_0 >= bit5_1:
        oxygen += '0'
        CO2 += '1'
    else:
        oxygen += '1'
        CO2 += '0'
    if bit6_0 >= bit6_1:
        oxygen += '0'
        CO2 += '1'
    else:
        oxygen += '1'
        CO2 += '0'
    if bit7_0 >= bit7_1:
        oxygen += '0'
        CO2 += '1'
    else:
        oxygen += '1'
        CO2 += '0'
    if bit8_0 >= bit8_1:
        oxygen += '0'
        CO2 += '1'
    else:
        oxygen += '1'
        CO2 += '0'
    if bit9_0 >= bit9_1:
        oxygen += '0'
        CO2 += '1'
    else:
        oxygen += '1'
        CO2 += '0'
    if bit10_0 >= bit10_1:
        oxygen += '0'
        CO2 += '1'
    else:
        oxygen += '1'
        CO2 += '0'
    if bit11_0 >= bit11_1:
        oxygen += '0'
        CO2 += '1'
    else:
        oxygen += '1'
        CO2 += '0'
    if bit12_0 >= bit12_1:
        oxygen += '0'
        CO2 += '1'
    else:
        oxygen += '1'
        CO2 += '0'

    CO2reports = reports.copy()
    OxygenReports = reports.copy()

    index = 0
    while len(CO2reports) > 1 and index <= 11:
        for line in CO2reports:
            if line[index] != CO2[index]:
                CO2reports.remove(line)
        index += 1

    if oxygen in OxygenReports:
        OxygenReports = [oxygen]
    else:
        index = 0
        while len(OxygenReports) > 1 and index <= 10:
            for line in OxygenReports:
                if line[:index+1] != oxygen[:index+1]:
                    OxygenReports.remove(line)
            index +=1

    CO2rating = int(CO2reports[0], 2)
    OxygenRating = int(OxygenReports[0], 2)

    print(CO2rating * OxygenRating)


if __name__ == '__main__':
    with open('test_binaryDiagnostics.txt') as x:
        report = x.readlines()
    for line in range(len(report)):
        report[line] = report[line][:-1]

    diagnosticReport2_2(report)


"""
--- Day 3: Binary Diagnostic ---
The submarine has been making some odd creaking noises, so you ask it to produce a diagnostic report just in case.

The diagnostic report (your puzzle input) consists of a list of binary numbers which, when decoded properly, can tell you many useful things about the conditions of the submarine. The first parameter to check is the power consumption.

You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the gamma rate and the epsilon rate). The power consumption can then be found by multiplying the gamma rate by the epsilon rate.

Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report. For example, given the following diagnostic report:

00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
Considering only the first bit of each number, there are five 0 bits and seven 1 bits. Since the most common bit is 1, the first bit of the gamma rate is 1.

The most common second bit of the numbers in the diagnostic report is 0, so the second bit of the gamma rate is 0.

The most common value of the third, fourth, and fifth bits are 1, 1, and 0, respectively, and so the final three bits of the gamma rate are 110.

So, the gamma rate is the binary number 10110, or 22 in decimal.

The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each position is used. So, the epsilon rate is 01001, or 9 in decimal. Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.

Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together. What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)

Your puzzle answer was 3277364.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
Next, you should verify the life support rating, which can be determined by multiplying the oxygen generator rating by the CO2 scrubber rating.

Both the oxygen generator rating and the CO2 scrubber rating are values that can be found in your diagnostic report - finding them is the tricky part. Both values are located using a similar process that involves filtering out values until only one remains. Before searching for either rating value, start with the full list of binary numbers from your diagnostic report and consider just the first bit of those numbers. Then:

Keep only numbers selected by the bit criteria for the type of rating value for which you are searching. Discard numbers which do not match the bit criteria.
If you only have one number left, stop; this is the rating value for which you are searching.
Otherwise, repeat the process, considering the next bit to the right.
The bit criteria depends on which type of rating value you want to find:

To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 1 in the position being considered.
To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 0 in the position being considered.
For example, to determine the oxygen generator rating value using the same example diagnostic report from above:

Start with all 12 numbers and consider only the first bit of each number. There are more 1 bits (7) than 0 bits (5), so keep only the 7 numbers with a 1 in the first position: 11110, 10110, 10111, 10101, 11100, 10000, and 11001.
Then, consider the second bit of the 7 remaining numbers: there are more 0 bits (4) than 1 bits (3), so keep only the 4 numbers with a 0 in the second position: 10110, 10111, 10101, and 10000.
In the third position, three of the four numbers have a 1, so keep those three: 10110, 10111, and 10101.
In the fourth position, two of the three numbers have a 1, so keep those two: 10110 and 10111.
In the fifth position, there are an equal number of 0 bits and 1 bits (one each). So, to find the oxygen generator rating, keep the number with a 1 in that position: 10111.
As there is only one number left, stop; the oxygen generator rating is 10111, or 23 in decimal.
Then, to determine the CO2 scrubber rating value from the same example above:

Start again with all 12 numbers and consider only the first bit of each number. There are fewer 0 bits (5) than 1 bits (7), so keep only the 5 numbers with a 0 in the first position: 00100, 01111, 00111, 00010, and 01010.
Then, consider the second bit of the 5 remaining numbers: there are fewer 1 bits (2) than 0 bits (3), so keep only the 2 numbers with a 1 in the second position: 01111 and 01010.
In the third position, there are an equal number of 0 bits and 1 bits (one each). So, to find the CO2 scrubber rating, keep the number with a 0 in that position: 01010.
As there is only one number left, stop; the CO2 scrubber rating is 01010, or 10 in decimal.
Finally, to find the life support rating, multiply the oxygen generator rating (23) by the CO2 scrubber rating (10) to get 230.
"""