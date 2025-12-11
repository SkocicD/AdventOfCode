nums = []
for l in open(0):
    if '+' not in l:
        nums.append(l)
    else:
        ops = list(l.split())

total = 0
opindex = 0
currnums = []
for n in zip(*nums):
    n = ''.join(n)
    n = n.strip()
    print(n)
    if n == '':
        if ops[opindex] == '+':
            total += sum(currnums)
        else:
            t = 1
            for n in currnums:
                t *= n
            total += t
        opindex += 1
        currnums = []
    else:
        currnums.append(int(n))
print(total)
