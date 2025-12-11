def betw(i, rng):
    return i >= rng[0] and i <= rng[1]


ranges = []
for l in open(0):
    if '-' in l:
        ranges.append(tuple(map(int, l.split('-'))))
ranges = sorted(ranges)
fresh = 0
i = 0
while i < len(ranges)-1:
    if betw(ranges[i+1][0], ranges[i]):
        if betw(ranges[i+1][1], ranges[i]):
            del ranges[i+1]
        else:
            ranges[i] = (ranges[i][0], ranges[i+1][1])
    else:
        i += 1

for rng in ranges:
    fresh += rng[1]-rng[0]+1
print(fresh)
