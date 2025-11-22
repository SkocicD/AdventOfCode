import sys


def around(r, c):
    global w, h
    ret = []
    if r > 0:
        ret.append((r-1, c))
    if r < h-1:
        ret.append((r+1, c))
    if c > 0:
        ret.append((r, c-1))
    if c < w-1:
        ret.append((r, c+1))
    return ret


def search(r, c):
    global board, nine_spots, searched
    val = board[r][c]
    if val == 9:
        return 1

    total = 0
    for rr, cc in around(r, c):
        if board[rr][cc] == val + 1:
            if (rr, cc) not in searched:
                total += search(rr, cc)
    return total


board = []

for line in sys.stdin:
    board.append(list(map(int, line[:-1])))
w = len(board[0])
h = len(board)
total = 0
for r in range(w):
    for c in range(h):
        if board[r][c] == 0:
            searched = set()
            total += search(r, c)
print(total)
