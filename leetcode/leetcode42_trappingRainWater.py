# -*- coding: utf-8 -*-
"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it is able to trap after raining.
"""
def trap(height):
    waterWalls = []
    for pos in range(len(height)): #rerunning positions between walls
        if height[pos+1] < height[pos]: #water starts when wall goes down
            startWall = pos #saves starting position of wall
            endFinder = pos + 1
            while (height[endFinder] < height[startWall]) #and (height[pos+1] < height[pos+2]): #checks next positions until finding one that stops water
                pos += 1
            endWall = nextPos
            waterWalls.append((startWall,endWall))
    return(waterWalls)
    
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))
"""
Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
          www  _
|      _   w  | |_ w _
|  _ w| |_   _|   |_| |__
|_| |_|   |_|
 0 1 2 3 4 5 6 7 8 9 10 11
"""