def part1(scanResults):
    increases = 0
    for i in range(1,len(scanResults)): # start at 1 because there are no indexes before 0
        if scanResults[i] > scanResults[i-1]:
            increases += 1

    print(increases)
    return increases

def part2(scanResults):
    increases = 0
    sums = []
    for i in range(len(scanResults)-2):
        sums.append(scanResults[i] + scanResults[i+1] + scanResults[i+2])
    part1(sums)
        



if __name__ == '__main__':
    with open('test_SonarSweep.txt') as x:
        scanResults = x.readlines()
        for i in range(len(scanResults)):
            scanResults[i] = int(scanResults[i])
    part2(scanResults)




"""
--- Day 1: Sonar Sweep ---
You're minding your own business on a ship at sea when the overboard alarm goes off! You rush to see if you can help. Apparently, one of the Elves tripped and accidentally sent the sleigh keys flying into the ocean!

Before you know it, you're inside a submarine the Elves keep ready for situations like this. It's covered in Christmas lights (because of course it is), and it even has an experimental antenna that should be able to track the keys if you can boost its signal strength high enough; there's a little meter that indicates the antenna's signal strength by displaying 0-50 stars.

Your instincts tell you that in order to save Christmas, you'll need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

As the submarine drops below the surface of the ocean, it automatically performs a sonar sweep of the nearby sea floor. On a small screen, the sonar sweep report (your puzzle input) appears: each line is a measurement of the sea floor depth as the sweep looks further and further away from the submarine.

For example, suppose you had the following report:

199
200
208
210
200
207
240
269
260
263
This report indicates that, scanning outward from the submarine, the sonar sweep found depths of 199, 200, 208, 210, and so on.

The first order of business is to figure out how quickly the depth increases, just so you know what you're dealing with - you never know if the keys will get carried into deeper water by an ocean current or a fish or something.

To do this, count the number of times a depth measurement increases from the previous measurement.
"""