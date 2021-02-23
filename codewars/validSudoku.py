import math

class Sudoku(object):
    def __init__(self, data):
        self.board = data
    def is_valid(self):
        cols = []
        for x in range(len(self.board)): # makes a list for each column on the board
            cols.append([])

        if math.sqrt(len(self.board)) != int(math.sqrt(len(self.board))):
            return False # check dimensions

        for row in self.board: # checks every row for the proper numbers and builds columns
            if math.sqrt(len(row)) != int(math.sqrt(len(row))): # checks dimensions
                return False
            for x in range(len(row)):
                if type(row[x]) is not int:
                    return False
                cols[x].append(row[x]) # appends elements from each row to proper column
            check = row.copy() # copy row to check to avoid changing sudoku
            check.sort() # sort row before comparing to list
            if check != list(range(1,len(row)+1)): # compares to a list from 1 to the length of the row
                return False
        for col in cols: # checks every column for the proper size and numbers
            if math.sqrt(len(col)) != int(math.sqrt(len(col))):
                return False
            check = col.copy()
            check.sort()
            if check != list(range(1,len(col)+1)):
                return False

        littleSquareSize = int(math.sqrt(len(cols))) # number of little squares in a row and dimensions
        littleSquares = []  # make a list to hold the smaller squares
        for row in range(0,len(self.board),littleSquareSize): # step size is size of the boxes so we start at the top of each box
            for y in range(littleSquareSize):
                littleSquares.append([]) # makes empty list to hold each smaller square
            currentSquare = -littleSquareSize  # used for indexing little square
            for element in range(0,len(self.board),littleSquareSize): # copies each row into the proper little squares
                currentRow = 0
                while currentRow < littleSquareSize: # currentSquare starts at -boxSize and is incremented
                    for num in self.board[row+currentRow][element:element+littleSquareSize]:
                        littleSquares[currentSquare].append(num)
                    currentRow += 1
                currentSquare += 1  # appends [0][0,1,2] then [1][0,1,2] then 2[0,1,2] then [0][3,4,5] and so on

        for square in littleSquares: # check each square for 1-9
            check = square.copy()
            check.sort()
            if check != list(range(1, len(self.board)+1)):
                return False

        return True # valid sudoku

x = Sudoku([
  [7,8,4,  1,5,9,  3,2,6],
  [5,3,9,  6,7,2,  8,4,1],
  [6,1,2,  4,3,8,  7,5,9],
  [9,2,8,  7,1,5,  4,6,3],
  [3,5,7,  8,4,6,  1,9,2],
  [4,6,1,  9,2,3,  5,8,7],
  [8,7,6,  3,9,4,  2,1,5],
  [2,4,3,  5,6,1,  9,7,8],
  [1,9,5,  2,8,7,  6,3,4]
])

"""
Given a Sudoku data structure with size NxN, N > 0 and √N == integer, write a method to validate if it has been filled out correctly.

The data structure is a multi-dimensional Array, i.e:

[
  [7,8,4,  1,5,9,  3,2,6],
  [5,3,9,  6,7,2,  8,4,1],
  [6,1,2,  4,3,8,  7,5,9],

  [9,2,8,  7,1,5,  4,6,3],
  [3,5,7,  8,4,6,  1,9,2],
  [4,6,1,  9,2,3,  5,8,7],

  [8,7,6,  3,9,4,  2,1,5],
  [2,4,3,  5,6,1,  9,7,8],
  [1,9,5,  2,8,7,  6,3,4]
]

Rules for validation

    Data structure dimension: NxN where N > 0 and √N == integer
    Rows may only contain integers: 1..N (N included)
    Columns may only contain integers: 1..N (N included)
    'Little squares' (3x3 in example above) may also only contain integers: 1..N (N included)

"""