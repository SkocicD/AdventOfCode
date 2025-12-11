from itertools import product


def neighbors(r, c):
    global h, w
    nbs = []
    for i, j in product(range(r-1, r+2), range(c-1, c+2)):
        if i > -1 and i < h and j > -1 and j < w and (i, j) != (r, c):
            nbs.append((i, j))
    return nbs


board = []
for l in open(0):
    board.append(list(l)[:-1])

h = len(board)
w = len(board[0])
total = 0
removed = True
while removed:
    removed = False
    for r in range(h):
        for c in range(w):
            if board[r][c] != '@':
                continue
            ct = 0
            for nb in neighbors(r, c):
                i, j = nb
                if board[i][j] == '@':
                    ct += 1
            if ct < 4:
                removed = True
                board[r][c] = 'x'
                total += 1
print(total)
