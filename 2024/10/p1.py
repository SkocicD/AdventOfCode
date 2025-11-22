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
    searched.add((r, c))
    val = board[r][c]
    if val == 9:
        nine_spots.add((r, c))

    for rr, cc in around(r, c):
        if board[rr][cc] == val + 1:
            if (rr, cc) not in searched:
                search(rr, cc)


board = []

for line in sys.stdin:
    board.append(list(map(int, line[:-1])))
w = len(board[0])
h = len(board)
total = 0
for r in range(w):
    for c in range(h):
        if board[r][c] == 0:
            nine_spots = set()
            searched = set()
            search(r, c)
            total += len(nine_spots)
print(total)
