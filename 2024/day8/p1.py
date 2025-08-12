import sys
from collections import defaultdict
freqs = defaultdict(set)
rows = 0
cols = 0
for r, line in enumerate(sys.stdin):
    for c, ch in enumerate(line[:-1]):
        cols = max(c+1, cols)
        if ch != '.':
            freqs[ch].add((r, c))
    rows = max(r+1, rows)

antinodes = set()
for f in freqs:
    ants = list(freqs[f])
    for ant in ants:
        for antt in ants:
            if ant != antt:
                rowdiff = ant[0]-antt[0]
                coldiff = ant[1]-antt[1]
                r = ant[0] + rowdiff
                c = ant[1] + coldiff
                if r >= 0 and r < rows and c >= 0 and c < cols:
                    antinodes.add((r, c))
                r = antt[0] - rowdiff
                c = antt[1] - coldiff
                if r >= 0 and r < rows and c >= 0 and c < cols:
                    antinodes.add((r, c))
print(len(antinodes))
