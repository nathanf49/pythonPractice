### TODO unclear on what happens after x reaches 0. Does it go negative or does it just drop down?

def main():
    xRange = list(range(155,182))
    yRange = list(range(-67,117))
    maxHeight = 0
    shotRange = 500  # shotRange = 25, answer 300 is too low, 124750 is too high
    for xVelocity in range(50):
        for yVelocity in range(shotRange):
            yHeight = probeSteps(xVelocity, yVelocity, xRange, yRange)
            if yHeight > maxHeight:
                maxHeight = yHeight

    print(maxHeight)


def probeSteps(xVelocity, yVelocity, xRange, yRange):
    """ Finds all positions of shot, returns the maximum y value/ height the shot achieves if it hits the target,
    otherwise returns 0 (0 is where y starts, so the maximum y value can never be below 0 """

    xPosition = 0  # start at [0,0]
    yPosition = 0
    positions = []  # keeps a list of all positions from shot
    yMax = 0
    hitsTarget = False  # Flag to check if shot is valid, assume shot doesn't hit target until it does
    while xVelocity > 0 or yVelocity > 0:
        xPosition += xVelocity
        yPosition += yVelocity
        positions.append([xPosition, yPosition])
        if xPosition in xRange and yPosition in yRange:
            hitsTarget = True  # shot is valid. Must stop in the range to be valid
        elif (xPosition in xRange) and (xVelocity == 0) and (yPosition > min(yRange)):
            hitsTarget = True  # shot will keep dropping until it is in range if it isn't moving along x axis
        if xVelocity > 0:  # xVelocity changes by 1 toward 0 due to drag
            xVelocity -= 1
        elif xVelocity < 0:
            xVelocity += 1
        yVelocity -= 1  # yvelocity changes by 1 due to gravity

    if hitsTarget is True:  # only update yMax on valid shots
        for position in positions:
            if position[1] > yMax:
                yMax = position[1]

    return yMax


if __name__ == '__main__':
    main()


"""
--- Day 17: Trick Shot ---
You finally decode the Elves' message. HI, the message says. You continue searching for the sleigh keys.

Ahead of you is what appears to be a large ocean trench. Could the keys have fallen into it? You'd better send a probe 
to investigate.

The probe launcher on your submarine can fire the probe with any integer velocity in the x (forward) and y (upward, or 
downward if negative) directions. For example, an initial x,y velocity like 0,10 would fire the probe straight up, while 
an initial velocity like 10,-1 would fire the probe forward at a slight downward angle.

The probe's x,y position starts at 0,0. Then, it will follow some trajectory by moving in steps. On each step, these 
changes occur in the following order:

The probe's x position increases by its x velocity.
The probe's y position increases by its y velocity.
Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, it decreases by 1 if it is greater than 0, 
increases by 1 if it is less than 0, or does not change if it is already 0.
Due to gravity, the probe's y velocity decreases by 1.
For the probe to successfully make it into the trench, the probe must be on some trajectory that causes it to be within 
a target area after any step. The submarine computer has already calculated this target area (your puzzle input). 
For example:

target area: x=20..30, y=-10..-5
This target area means that you need to find initial x,y velocity values such that after any step, the probe's x 
position is at least 20 and at most 30, and the probe's y position is at least -10 and at most -5.

Given this target area, one initial velocity that causes the probe to be within the target area after any step is 7,2:

.............#....#............
.......#..............#........
...............................
S........................#.....
...............................
...............................
...........................#...
...............................
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................TTTTTTTT#TT
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................TTTTTTTTTTT
In this diagram, S is the probe's initial position, 0,0. The x coordinate increases to the right, and the y coordinate 
increases upward. In the bottom right, positions that are within the target area are shown as T. After each step 
(until the target area is reached), the position of the probe is marked with #. (The bottom-right # is both a position 
the probe reaches and a position in the target area.)

Another initial velocity that causes the probe to be within the target area after any step is 6,3:

...............#..#............
...........#........#..........
...............................
......#..............#.........
...............................
...............................
S....................#.........
...............................
...............................
...............................
.....................#.........
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................T#TTTTTTTTT
....................TTTTTTTTTTT
Another one is 9,0:

S........#.....................
.................#.............
...............................
........................#......
...............................
....................TTTTTTTTTTT
....................TTTTTTTTTT#
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................TTTTTTTTTTT
One initial velocity that doesn't cause the probe to be within the target area after any step is 17,-4:

S..............................................................
...............................................................
...............................................................
...............................................................
.................#.............................................
....................TTTTTTTTTTT................................
....................TTTTTTTTTTT................................
....................TTTTTTTTTTT................................
....................TTTTTTTTTTT................................
....................TTTTTTTTTTT..#.............................
....................TTTTTTTTTTT................................
...............................................................
...............................................................
...............................................................
...............................................................
................................................#..............
...............................................................
...............................................................
...............................................................
...............................................................
...............................................................
...............................................................
..............................................................#
The probe appears to pass through the target area, but is never within it after any step. Instead, it continues down and 
to the right - only the first few steps are shown.

If you're going to fire a highly scientific probe out of a super cool probe launcher, you might as well do it with 
style. How high can you make the probe go while still reaching the target area?

In the above example, using an initial velocity of 6,9 is the best you can do, causing the probe to reach a maximum y 
position of 45. (Any higher initial y velocity causes the probe to overshoot the target area entirely.)

Find the initial velocity that causes the probe to reach the highest y position and still eventually be within the 
target area after any step. What is the highest y position it reaches on this trajectory?
"""