nums = []
for l in open(0):
    if l[0].isnumeric():
        nums.append(list(map(int, l.split())))
    else:
        ops = list(l.split())

total = 0
for i, ns in enumerate(zip(*nums)):
    if ops[i] == '+':
        total += sum(ns)
    else:
        t = 1
        for n in ns:
            t *= n
        total += t
print(total)
