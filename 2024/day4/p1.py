board = open('input.txt','r').read()
board = board.split('\n')[:-1]

def N(r, c):
    if r < 3:
        return 0
    if board[r-1][c] == 'M' and board[r-2][c] == 'A' and board[r-3][c] == 'S':
        return 1
    return 0
def S(r, c):
    if r > len(board) - 4:
        return 0
    if board[r+1][c] == 'M' and board[r+2][c] == 'A' and board[r+3][c] == 'S':
        return 1
    return 0
def W(r, c):
    if c < 3:
        return 0
    if board[r][c-1] == 'M' and board[r][c-2] == 'A' and board[r][c-3] == 'S':
        return 1
    return 0
def E(r, c):
    if c > len(board[0]) - 4:
        return 0
    if board[r][c+1] == 'M' and board[r][c+2] == 'A' and board[r][c+3] == 'S':
        return 1
    return 0
def NW(r, c):
    if r < 3 or c < 3:
        return 0
    if board[r-1][c-1] == 'M' and board[r-2][c-2] == 'A' and board[r-3][c-3] == 'S':
        return 1
    return 0
def NE(r, c):
    if r < 3 or c > len(board[0]) - 4:
        return 0
    if board[r-1][c+1] == 'M' and board[r-2][c+2] == 'A' and board[r-3][c+3] == 'S':
        return 1
    return 0
def SE(r, c):
    if r > len(board) - 4 or c > len(board[0]) - 4:
        return 0
    if board[r+1][c+1] == 'M' and board[r+2][c+2] == 'A' and board[r+3][c+3] == 'S':
        return 1
    return 0
def SW(r, c):
    if r > len(board) - 4 or c < 3: 
        return 0
    if board[r+1][c-1] == 'M' and board[r+2][c-2] == 'A' and board[r+3][c-3] == 'S':
        return 1
    return 0

total = 0
for r, row in enumerate(board):
    for c, char in enumerate(row):
        if char == 'X':
            total += N(r,c) + S(r,c) + E(r,c) + W(r,c) + NE(r,c) + NW(r,c) + SE(r,c) + SW(r,c)



print(total)



