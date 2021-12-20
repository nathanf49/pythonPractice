import math
import numpy as np

def smokeBasin(heightMap):
    riskLevel = 0 # sum of each low point + 1
    for height in range(len(heightMap[:,0])):
        for width in range(len(heightMap[0])): # check all locations on heightMap
            surroundingPointValues = []
            if height - 1 < 0 and width -1 < 0: # bottom left corner
                surroundingPointValues += [heightMap[height, width+1], heightMap[height+1,width]]
            elif height - 1 < 0 and width + 1 > 99: # bottom right corner
                surroundingPointValues += [heightMap[height+1,width], heightMap[height,width-1]]
            elif height + 1 > 99 and width -1 < 0: # top left corner
                surroundingPointValues += [heightMap[height-1,width],heightMap[height,width+1]]
            elif height + 1 > 99 and width + 1 > 99: # top right corner
                surroundingPointValues += [heightMap[height, width-1], heightMap[height-1,width]]
            elif height + 1 > 99: # top line, width must be in range or it would have been filtered out above
                surroundingPointValues += [heightMap[height,width + 1], heightMap[height,width-1], heightMap[height-1,width]]
            elif height - 1 < 0: # bottom line, width in range
                surroundingPointValues += [heightMap[height, width + 1], heightMap[height, width - 1],heightMap[height + 1, width]]
            elif width + 1 > 99: # right side, height in range
                surroundingPointValues += [heightMap[height+1,width], heightMap[height-1,width], heightMap[height,width-1]]
            elif width -1 < 0: # left side, height in range
                surroundingPointValues += [heightMap[height+1,width], heightMap[height-1,width], heightMap[height,width+1]]
            else: # everything in range
                surroundingPointValues += [heightMap[height+1,width],heightMap[height-1,width],heightMap[height,width+1],heightMap[height,width-1]]
            try:
                if heightMap[height,width] < min(surroundingPointValues): # if point we're checking is greater than the max of surrounding height values it will be greater than all others
                    riskLevel += heightMap[height,width] + 1
            except:
                print(height,width)

    print(riskLevel)

def smokeBasin2(heightMap):
    riskLevel = [] # multiply top 3
    for height in range(len(heightMap[:,0])):
        for width in range(len(heightMap[0])): # check all locations on heightMap
            surroundingPointValues = []
            if height - 1 < 0 and width -1 < 0: # bottom left corner
                surroundingPointValues += [heightMap[height, width+1], heightMap[height+1,width]]
            elif height - 1 < 0 and width + 1 > 99: # bottom right corner
                surroundingPointValues += [heightMap[height+1,width], heightMap[height,width-1]]
            elif height + 1 > 99 and width -1 < 0: # top left corner
                surroundingPointValues += [heightMap[height-1,width],heightMap[height,width+1]]
            elif height + 1 > 99 and width + 1 > 99: # top right corner
                surroundingPointValues += [heightMap[height, width-1], heightMap[height-1,width]]
            elif height + 1 > 99: # top line, width must be in range or it would have been filtered out above
                surroundingPointValues += [heightMap[height,width + 1], heightMap[height,width-1], heightMap[height-1,width]]
            elif height - 1 < 0: # bottom line, width in range
                surroundingPointValues += [heightMap[height, width + 1], heightMap[height, width - 1],heightMap[height + 1, width]]
            elif width + 1 > 99: # right side, height in range
                surroundingPointValues += [heightMap[height+1,width], heightMap[height-1,width], heightMap[height,width-1]]
            elif width -1 < 0: # left side, height in range
                surroundingPointValues += [heightMap[height+1,width], heightMap[height-1,width], heightMap[height,width+1]]
            else: # everything in range
                surroundingPointValues += [heightMap[height+1,width],heightMap[height-1,width],heightMap[height,width+1],heightMap[height,width-1]]
            if heightMap[height,width] > max(surroundingPointValues): # if point we're checking is greater than the max of surrounding height values it will be greater than all others
                riskLevel.append(heightMap[height,width])
    riskLevel.sort()
    riskLevel = riskLevel[-1] * riskLevel[-2] * riskLevel[-3]
    print(riskLevel)

if __name__ == '__main__':
    with open('test_smokeBasin.txt') as file:
        inputData = file.read()
    file.close()
    #inputData = '21999432103987894921985678989287678967899899965678'
    inputList = []
    for i in range(len(inputData)): # convert string to list of ints, so we can work with an array instead of str
        try:
            inputList.append(int(inputData[i]))
        except ValueError:
            pass

    mapDimensions = int(math.sqrt(len(inputList))) # get dimensions of 2d array, assumes square array
    map = np.array(inputList)
    #map = map.reshape(mapDimensions,mapDimensions) # make map 2 dimensional
    map = map.reshape(mapDimensions,mapDimensions)
    smokeBasin2(map) # 729 is too low



"""
--- Day 9: Smoke Basin ---
These caves seem to be lava tubes. Parts are even still volcanically active; small hydrothermal vents release smoke into the caves that slowly settles like rain.

If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer. The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).

Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:

2199943210
3987894921
9856789892
8767896789
9899965678
Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.

Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)

In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0), one is in the third row (a 5), and one is in the bottom row (also a 5). All other locations on the heightmap have some lower adjacent location, and so are not low points.

The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels of all low points in the heightmap is therefore 15.

Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?

Your puzzle answer was 465.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
Next, you need to find the largest basins so you know what areas are most important to avoid.

A basin is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin, although some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations will always be part of exactly one basin.

The size of a basin is the number of locations within the basin, including the low point. The example above has four basins.

The top-left basin, size 3:

2199943210
3987894921
9856789892
8767896789
9899965678
The top-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678
The middle basin, size 14:

2199943210
3987894921
9856789892
8767896789
9899965678
The bottom-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678
Find the three largest basins and multiply their sizes together. In the above example, this is 9 * 14 * 9 = 1134.

What do you get if you multiply together the sizes of the three largest basins?
"""