sum = 0
for r in open(0):
    r = list(r)[:-1]
    mx = ['0']*12
    mxi = [0]*12
    for i in range(12):
        f = mxi[i-1]+1 if i > 0 else 0
        for j, c in enumerate(r[f:]):
            if j+f == len(r)-(11-i):
                break
            if c > mx[i]:
                mx[i] = c
                mxi[i] = f+j
    sum += int(''.join(mx))

print(sum)
