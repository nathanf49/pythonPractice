# -*- coding: utf-8 -*-
"""Given a m * n matrix mat of ones (representing soldiers) and zeros (representing civilians), return the indexes of
the k weakest rows in the matrix ordered from the weakest to the strongest.

A row i is weaker than row j, if the number of soldiers in row i is less than the number of soldiers in row j,
or they have the same number of soldiers but i is less than j. Soldiers are always stand in the frontier of a row,
that is, always ones may appear first and then zeros. """


def kWeakestRows(mat, k):
    rowName = 0
    out = []
    for row in mat:
        row.append(sum(row))  # puts score on end
        row.append(rowName)  # puts rowName on end
        rowName += 1
    while k > 0:
        weak = [99999999, 0]  # initialize weakest row at extremely high score and row number
        for row in mat:  # finds weakest row
            if row[-2] < weak[0]:  # row[-2] is score
                weak[0] = row[-2]
                weak[1] = row[-1]  # row[-1] is name
        out.append(weak[1])
        mat[weak[1]][-2] = 99999999  # set score very high so it won't come up as min score agian
        k -= 1
    return out


matrix = [[1, 1, 0, 0, 0],
          [1, 1, 1, 1, 0],
          [1, 0, 0, 0, 0],
          [1, 1, 0, 0, 0],
          [1, 1, 1, 1, 1]]
rows = 3
print(kWeakestRows(matrix, rows))
"""
Example 1:
    
Input: mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
Output: [2,0,3]
Explanation: 
The number of soldiers for each row is: 
row 0 -> 2 
row 1 -> 4 
row 2 -> 1 
row 3 -> 2 
row 4 -> 5 
Rows ordered from the weakest to the strongest are [2,0,3,1,4]

Example 2:

Input: mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2
Output: [0,2]
Explanation: 
The number of soldiers for each row is: 
row 0 -> 1 
row 1 -> 4 
row 2 -> 1 
row 3 -> 1 
Rows ordered from the weakest to the strongest are [0,2,3,1
"""
