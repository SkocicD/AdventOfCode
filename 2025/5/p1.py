def betw(ing, rng):
    return ing >= rng[0] and ing <= rng[1]


ranges = []
ingredients = []
for l in open(0):
    if '-' in l:
        ranges.append(tuple(map(int, l.split('-'))))
    elif l != '\n':
        ingredients.append(int(l[:-1]))
ranges = sorted(ranges)
fresh = 0
for ing in ingredients:
    for rng in ranges:
        if betw(ing, rng):
            fresh += 1
            break
print(fresh)
