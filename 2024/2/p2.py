from itertools import pairwise
with open("input.txt",'r') as f:
     lines = f.read().split("\n")[:-1]

def checkSafe(levels):
    inc = (levels[0]<levels[1])
    for adj in pairwise(levels):
        if (adj[0] < adj[1]) != inc:
            return False
        diff = abs(adj[0]-adj[1])
        if diff < 1 or diff > 3:
            return False
    else:
        return True
    

safe = 0
for line in lines:
    levels = list(map(int, line.split()))
    for i in range(len(levels)):
        if checkSafe(levels[0:i]+levels[i+1:]):
            safe+=1
            break

print(safe)
