from itertools import pairwise
with open("input.txt",'r') as f:
     lines = f.read().split("\n")[:-1]

safe = 0
for line in lines:
    levels = list(map(int, line.split()))
    inc = (levels[0] < levels[1])
    for adj in pairwise(levels):
        if (adj[0] < adj[1]) != inc:
            break
        diff = abs(adj[0]-adj[1])
        if diff < 1 or diff > 3:
            break
    else:
        safe += 1

print(safe)
