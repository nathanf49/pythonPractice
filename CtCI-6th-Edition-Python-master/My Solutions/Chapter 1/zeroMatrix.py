# O(m x n)
"""
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.
"""


def zeroMatrix(matrix):
    zeroColumns = []  # list to store which columns should be set to 0
    for row in range(len(matrix)):
        zeroRow = False  # variable to keep track of whether or not row should be 0'd after checking it
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0:
                zeroRow = True  # mark row to be zero'd
                if col not in zeroColumns:
                    zeroColumns.append(col)  # saves column to be 0'd later

        if zeroRow is True:
            matrix[row] = [0] * len(matrix[row])  # sets row to all zeros before moving to the next row if there was a 0

    for row in range(len(matrix)):  # sets columns to 0
        for col in zeroColumns:
            matrix[row][col] = 0

    return matrix


test = [[0, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 0]]

out = zeroMatrix(test)
for x in out:  # print with formatting
    print(x)
