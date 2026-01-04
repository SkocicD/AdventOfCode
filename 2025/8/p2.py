import ctypes

coords = []
dists = []
for l in open(0):
    coords.append(tuple(map(int, l.split(','))))
for i, coord in enumerate(coords):
    for coord2 in coords[i+1:]:
        dist = sum((coord[i] - coord2[i])**2 for i in [0, 1, 2])**.5
        dists.append((dist, coord, coord2))
dists = sorted(dists)
pools = {c: {c} for c in coords}

for _, c1, c2 in dists:
    s = pools[c1] | pools[c2]
    for c in s:
        pools[c] = s

    ids = set(map(id, [pools[p] for p in pools]))
    pp = [ctypes.cast(setid, ctypes.py_object).value for setid in ids]
    if len(pp) == 1:
        print(c1[0]*c2[0])
        exit()
