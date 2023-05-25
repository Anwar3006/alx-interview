#!/usr/bin/python3
"""
The N–queens puzzle is the problem of placing N chess queens on an N × N
chessboard so that no two queens threaten each other. Thus, the solution
requires that no two queens share the same row, column, or diagonal.
"""
import sys

Result = []


def isSafe(board, row, column):
    """
    Function checks if the current coordinate is safe for inserting 
    a Queen by checking from the current coordinate to the left 
    diagonals and row
    """
    # for each column check row for presense of Queen
    for i in range(row):
        if board[i][column] == 'Q':
            return False

    # check left upper diagonal(\) for presense of Queen
    i, j = row, column
    while (i >= 0) and (j >= 0):
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # check left lower diagonal(/) for presense of Queen
    i, j = row, column
    while (i >= 0) and (j < len(board)):
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1
    return True


def SolveNQueen(board, row):
    """
    Recursively checks which coordinate to place Queen and
    Uses Backtracking to undo placements if coordinate is unfit
    """
    # base case for recursion
    if row == len(board):
        lst = []
        for i in range(0, len(board)):
            for j in range(0, len(board)):
                if board[i][j] == 'Q':
                    lst.append([i, j])
        return Result.append(lst)

    # Check which coordinate to place Queen
    for column in range(len(board)):
        if isSafe(board, row, column):
            board[row][column] = 'Q'
            # after inserting Queen check the next row in the
            # same column for possible placement of another Queen
            SolveNQueen(board, row + 1)
            # Backtrack and reset if coordinate isn't suitable
            board[row][column] = '-'


def get_Number_of_Queens():
    """
    Get the number of queens
    """
    if len(sys.argv) < 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            exit(1)
    except ValueError:
        print("N must be a number")
        exit(1)
    return N


if __name__ == "__main__":
    N = get_Number_of_Queens()
    row = 0
    board = [['-' for j in range(0, N)] for i in range(0, N)]
    SolveNQueen(board, row)

    for i in Result:
        print(i)
