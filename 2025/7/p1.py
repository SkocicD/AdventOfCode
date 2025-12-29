from time import sleep


def step(r, c):
    global h, seen
    if r+1 == h:
        return None
    else:
        if (r+1, c) in seen:
            return None
        return (r+1, c)


board = []
for l in open(0):
    board.append(list(l)[:-1])

start = (0, board[0].index("S"))
h = len(board)
w = len(board[0])
stack = [start]
splitters = set()
seen = set()
while len(stack):
    seen.add(stack[-1])
    next = step(*stack.pop())
    if not next:
        continue
    r, c = next
    if board[r][c] == '.':
        stack.append(next)
        seen.add(next)
    else:
        stack.append((r, c-1))
        stack.append((r, c+1))
        seen.add((r, c+1))
        seen.add((r, c-1))
        splitters.add((r, c))
print(len(splitters))
