# both O(nxn)
"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to
rotate the image by 90 degrees. Can you do this in place?
"""
def clockwise(matrix):
    n = len(matrix)
    updated = []
    for x in range(n): # for some reason, making a copy still changes both matricies even though the whole point of
        # making a copy is so that doesn't happen. not sure why
        updated.append([None] * n)
    for row in range(n):
        for col in range(n):
            updated[row][col] = matrix[n-col-1][row]
    return updated

def counterClockwise(matrix):
    n = len(matrix)
    updated = []
    for x in range(n):  # for some reason, making a copy still changes both matricies even though the whole point of
        # making a copy is so that doesn't happen. not sure why
        updated.append([None] * n)
    for row in range(n):
        for col in range(n):
            updated[row][col] = matrix[col][n-row-1]
    return updated

test = [[1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25]]

out = counterClockwise(test)
for row in out:
    print(row)
