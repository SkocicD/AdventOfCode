for r in open(0):
    r = r.split(',')
sum = 0
for rng in r:
    low, high = map(int, rng.split('-'))
    for n in range(low, high+1):
        s = str(n)
        l = len(s)
        h = int(l/2)
        if not (l % 2) and s[:h] == s[h:]:
            sum += n
print(sum)
