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
    global board
    if (r, c) in searched:
        return (0, 0)
    searched.add((r, c))
    crop = board[r][c]

    perim = 4
    area = 1
    for rr, cc in around(r, c):
        if board[rr][cc] == crop:
            perim -= 1
            p, a = search(rr, cc)
            perim += p
            area += a
    return (perim, area)


board = []

for line in sys.stdin:
    board.append(list(line[:-1]))
w = len(board[0])
h = len(board)
searched = set()
total = 0

for r in range(w):
    for c in range(h):
        p, a = search(r, c)
        total += p*a
print(total)
