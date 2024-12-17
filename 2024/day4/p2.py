board = open('input.txt','r').read()
board = board.split('\n')[:-1]

def left(r,c):
    if r > len(board) - 3 or c > len(board[0]) - 3:
        return 0
    if board[r][c+2] == 'S' and board[r+1][c+1] == 'A' and board[r+2][c] == 'M' and board[r+2][c+2] == 'S':
        return 1
    return 0

def right(r,c):
    if r < 2 or c < 2:
        return 0
    if board[r][c-2] == 'S' and board[r-1][c-1] == 'A' and board[r-2][c] == 'M' and board[r-2][c-2] == 'S':
        return 1
    return 0

def top(r,c):
    if r > len(board) - 3 or c < 2: 
        return 0
    if board[r+2][c] == 'S' and board[r+1][c-1] == 'A' and board[r][c-2] == 'M' and board[r+2][c-2] == 'S':
        return 1
    return 0

def bottom(r,c):
    if r < 2 or c > len(board[0]) - 3:
        return 0
    if board[r-2][c] == 'S' and board[r-1][c+1] == 'A' and board[r][c+2] == 'M' and board[r-2][c+2] == 'S':
        return 1
    return 0

total = 0
for r, row in enumerate(board):
    for c, char in enumerate(row):
        if char == 'M':
            total += left(r,c) + right(r,c) + top(r,c) + bottom(r,c)

print(total)
