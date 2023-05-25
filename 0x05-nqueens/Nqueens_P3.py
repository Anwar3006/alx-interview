result = []
 
# A utility function to print solution
 
 
''' A utility function to check if a queen can
be placed on board[row][col]. Note that this
function is called when "col" queens are
already placed in columns from 0 to col -1.
So we need to check only left side for
attacking queens '''
 
 
# def isAttacking(row, column, board, N):
# Function to check if two queens threaten each other or not
def isSafe(r, c, board):

	# return false if two queens share the same column
	for i in range(r):
		if board[i][c] == 'Q':
			return False

	# return false if two queens share the same `\` diagonal
	(i, j) = (r, c)
	while i >= 0 and j >= 0:
		if board[i][j] == 'Q':
			return False
		i = i - 1
		j = j - 1

	# return false if two queens share the same `/` diagonal
	(i, j) = (r, c)
	while i >= 0 and j < len(board):
		if board[i][j] == 'Q':
			return False
		i = i - 1
		j = j + 1

	return True
 
 
''' A recursive utility function to solve N
Queen problem '''
 
 
def solveNQUtil(board, col, N):
    ''' base case: If all queens are placed
    then return true '''
    if (col == N):
        v = []
        for i in range(0, N):
            for j in range(0, N):
        # for i in board:
        #     for j in range(len(i)):
                if board[i][j] == 'Q':
                    v.append([i, j])
        result.append(v)
        return True
 
    ''' Consider this column and try placing
    this queen in all rows one by one '''
    res = False
    for row in range(N):
 
        ''' Check if queen can be placed on
        board[i][col] '''
        if (isSafe(row, col, board)):
 
            # Place this queen in board[i][col]
            board[row][col] = 'Q'
 
            # Make result true if any placement
            # is possible
            res = solveNQUtil(board, col + 1, N) or res
 
            ''' If placing queen in board[i][col]
            doesn't lead to a solution, then
            remove queen from board[i][col] '''
            board[row][col] = '-'  # BACKTRACK
 
    ''' If queen can not be place in any row in
        this column col then return false '''
    return res
 
 
''' This function solves the N Queen problem using
Backtracking. It mainly uses solveNQUtil() to
solve the problem. It returns false if queens
cannot be placed, otherwise return true and
prints placement of queens in the form of 1s.
Please note that there may be more than one
solutions, this function prints one of the
feasible solutions.'''
 
 
def solveNQ(N):
    result.clear()
    board = [['-' for j in range(N)]
             for i in range(N)]
    solveNQUtil(board, 0, N)
    result.sort()
    return result
 
 
# Driver Code
n = 4
res = solveNQ(n)
# print(res)
for row in res:
    print(row)
