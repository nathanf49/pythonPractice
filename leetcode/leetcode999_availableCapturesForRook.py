# -*- coding: utf-8 -*-
"""
On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.  
These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase characters represent white pieces, and 
lowercase characters represent black pieces.
The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south), 
then moves in that direction until it chooses to stop, reaches the edge of the board, 
or captures an opposite colored pawn by moving to the same square it occupies.  
Also, rooks cannot move into the same square as other friendly bishops.
Return the number of pawns the rook can capture in one move.
"""
def numRookCaptures(board):
    for row in range(len(board)):
        if "R" in board[row]:
            rookRow = row #saves row that rook can be in
            rookCol = board[row].index('R') #saves column that rook can be in
    ## Working by eliminating area that can't be captured
    for row in range(len(board)): #checks column for uncapturable area
        if (board[row][rookCol] == "B" or board[row][rookCol] == "p") and row < rookRow: #if a bishop is in the column the rook is in , but a lower row
            for x in range(0,row):
                if board[x] != [".",".",".",".",".",".",".","."]:
                    board[x] = [".",".",".",".",".",".",".","."] #clear all , no longer capturable
        elif (board[row][rookCol] == "B" or board[row][rookCol] == "p") and row > rookRow:#if a bishop is in the column the rook is in , but a higher row
            for x in range(row+1,len(board)):
                if board[x] != [".",".",".",".",".",".",".","."]:
                    board[x] = [".",".",".",".",".",".",".","."]#clear all , no longer capturable
    for col in range(len(board[rookRow])): # checks row for uncapturable area
        if (board[rookRow][col] == "B" or board[rookRow][col] == "p") and col < rookCol: #if bishop before rooke
            for x in range(len(board)):
                for y in range(0,col): #clear everything before rook
                    if board[x][y] != ".":
                        board[x][y] = "."
        elif (board[rookRow][col] == "B" or board[rookRow][col] == "p") and col > rookCol: #if bishop after rook
            for x in range(len(board)):
                for y in range(col+1,len(board)):
                    if board[x][y] != ".": #clear everything after rook
                        board[x][y] = "."
    pawnCount = 0
    for row in range(len(board)): #count pawns in column
        if board[row][rookCol] == "p":
            pawnCount += 1
    for col in range(len(board[rookRow])):
        if board[rookRow][col] == "p":
            pawnCount += 1
            
    return(pawnCount)
    
board =[[".",".",".",".",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        ["p","p",".","R",".","p","B","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".","B",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".",".",".",".",".","."]]
print(numRookCaptures(board))

"""
Input: [[".",".",".",".",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".","R",".",".",".","p"],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."]]
Output: 3
Explanation: 
In this example the rook is able to capture all the pawns.

Input: [[".",".",".",".",".",".",".","."],
        [".","p","p","p","p","p",".","."],
        [".","p","p","B","p","p",".","."],
        [".","p","B","R","B","p",".","."],
        [".","p","p","B","p","p",".","."],
        [".","p","p","p","p","p",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."]]
Output: 0
Explanation: 
Bishops are blocking the rook to capture any pawn.

Input: [[".",".",".",".",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        ["p","p",".","R",".","p","B","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".","B",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".",".",".",".",".","."]]

Output: 3
Explanation: 
The rook can capture the pawns at positions b5, d6 and f5.


    board.length == board[i].length == 8
    board[i][j] is either 'R', '.', 'B', or 'p'
    There is exactly one cell with board[i][j] == 'R'
"""