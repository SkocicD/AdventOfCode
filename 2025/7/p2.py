def step(r, c):
    global h, seen, board

    if (r, c) in seen:
        return seen[(r, c)]

    if r+1 == h:
        seen[(r, c)] = 1
        return 1

    if board[r][c] == '.':
        ret = step(r+1, c)
    else:
        ret = step(r, c+1) + step(r, c-1)

    seen[(r, c)] = ret
    return ret


board = []
for l in open(0):
    board.append(list(l)[:-1])

start = (0, board[0].index("S"))
h = len(board)
seen = {}
print(step(*start))
