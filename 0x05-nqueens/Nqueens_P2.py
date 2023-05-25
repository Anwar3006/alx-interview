import sys

# print("Enter the number")
# N = int(input())
result = []

def get_Queens():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        N = int(sys.argv[1]) 
        if N < 4:
            print("N must be at least 4")
            exit(1)
    except ValueError:
        print("N must be a number")
    return N

def isAttacking(row, column, board, N):
    for i in range(0, N):
        if board[row][i] == 'Q' or board[i][column] == 'Q':
            return False
    
    P_diagonal = row + column
    N_diagonal = row - column
    for i in range(0, N):
        for j in range(0, N):
            if i+j == P_diagonal or i-j == N_diagonal:
                if board[i][j] == 'Q':
                    return False
    return True


def solveNQ(board, column, N):
    if column == N:
        for i in board:
            for j in range(len(i)):
                if i[j] == 'Q':
                    result.append([i, j])
        return True
    
    state = False
    for row in range(N):
        if (not isAttacking(row, column, board, N)):
            board[row][column] = 'Q'

            if solveNQ(board, column + 1, N) == True:
                state = True
            board[row][column] = '-'
    return state

def NQ():
    N = get_Queens()
    result.clear()
    board = [['-' for j in range(N)] for i in range(N)]
    solveNQ(board, 0, N)
    result.sort()
    return result

print(NQ())


