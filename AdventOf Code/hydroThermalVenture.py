import numpy as np


def hydroThermalMap(coordinates):
    map = [0] * 1000000
    map = np.array(map)
    map = map.reshape(1000, 1000)
    for c in coordinates:
        if (c[1] == c[3]):  # vertical lines
            if c[2] > c[0]:  # counting from c[0] to c[2]
                for i in range(c[0], c[2] + 1):  # change first index to move to next line
                    map[i][c[1]] += 1
            else:  # counting from c[2] to c[0] for range
                for i in range(c[2], c[0] + 1):
                    map[i][c[1]] += 1

        elif (c[0] == c[2]):  # horizontal lines
            if c[3] > c[1]:  # counting from c[1] to c[3] for range
                for i in range(c[1], c[3] + 1):  # change second index to move across same line
                    map[c[0]][i] += 1
            else:  # counting from c[3] to c[1] for range
                for i in range(c[3], c[1] + 1):
                    map[c[0]][i] += 1

        else:  # diagonal, do not make a line
            continue  # moves to next line in coordinates

    score = np.count_nonzero(map > 1)
    print(score)


def hydroThermalMap2(coordinates):  # part 2, now include diagonal lines
    map = [0] * 1000000
    map = np.array(map)
    map = map.reshape(1000, 1000)
    for c in coordinates:
        original = c
        if (c[1] == c[3]):  # vertical lines
            if c[2] > c[0]:  # counting from c[0] to c[2]
                for i in range(c[0], c[2] + 1):  # change first index to move to next line
                    map[i][c[1]] += 1
            else:  # counting from c[2] to c[0] for range
                for i in range(c[2], c[0] + 1):
                    map[i][c[1]] += 1

        elif (c[0] == c[2]):  # horizontal lines
            if c[3] > c[1]:  # counting from c[1] to c[3] for range
                for i in range(c[1], c[3] + 1):  # change second index to move across same line
                    map[c[0]][i] += 1
            else:  # counting from c[3] to c[1] for range
                for i in range(c[3], c[1] + 1):
                    map[c[0]][i] += 1

        else:  # diagonal, must be 45 degrees to make a line
            if diagonalCheck45degrees(c) == False:
                continue  # moves to next line in coordinates
            else:  # diagonal is on a 45 degree line
                if c[2] > c[0]:
                    for i in range(c[0], c[2] + 1):  # counts from top down
                        map[i][c[1]] += 1 # i starts with first pair of coordinates, so adjust c[1]
                        if (c[1] >= c[3]):  # diagonal down and left
                            c[1] -= 1
                        else:  # diagonal down and right
                            c[1] += 1

                else:  # c[0] > c[2]
                    for i in range(c[2], c[0] + 1):  # counts from bottom up
                        try:
                            map[i][c[3]] += 1 # i starts with second pair of coordinates , so adjust c[3]
                        except:
                            pass
                        if (c[3] >= c[1]):  # up and left
                            c[3] -= 1
                        else:
                            c[3] += 1  # up and right

    score = np.count_nonzero(map > 1)
    print(score)


def diagonalCheck45degrees(c):
    if c[0] > c[2]:
        firstIndex = c[0] - c[2]
    else:
        firstIndex = c[2] - c[0]

    if c[1] > c[3]:
        secondIndex = c[1] - c[3]
    else:
        secondIndex = c[3] - c[1]

    return firstIndex == secondIndex


if __name__ == '__main__':
    with open('test_hydroThermalVenture.txt') as f:
        inputData = f.readlines()
        f.close()

    for i in range(len(inputData)):  # splits strings into lists
        inputData[i] = inputData[i].split()
        del inputData[i][1]  # removes arrow from data as it's unneeded
        inputData[i][0] = inputData[i][0].split(',')
        inputData[i][1] = inputData[i][1].split(',')
        inputData[i] = [int(inputData[i][0][0]), int(inputData[i][0][1]), int(inputData[i][1][0]),
                        int(inputData[i][1][1])]

    hydroThermalMap2(inputData)

"""
--- Day 5: Hydrothermal Venture ---
You come across a field of hydrothermal vents on the ocean floor! These vents constantly produce large, opaque clouds, so it would be best to avoid them if possible.

They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input) for you to review. For example:

0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. In other words:

An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

So, the horizontal and vertical lines from the above list would produce the following diagram:

.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....
In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.

Consider only horizontal and vertical lines. At how many points do at least two lines overlap?
"""

"""--- Part Two ---
Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.

Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:

An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
Considering all lines from the above example would now produce the following diagram:

1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111....
You still need to determine the number of points where at least two lines overlap. In the above example, this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.

Consider all of the lines. At how many points do at least two lines overlap?"""
