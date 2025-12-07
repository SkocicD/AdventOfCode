for r in open(0):
    r = r.split(',')
sum = 0
for rng in r:
    low, high = map(int, rng.split('-'))
    for n in range(low, high+1):
        s = str(n)
        l = len(s)
        added = False
        for i in range(2, len(s)+1):
            h = int(l/i)
            if not (l % i) and s == s[:h]*i:
                sum += n
                # print(n)
                break
        if added:
            continue
print(sum)
