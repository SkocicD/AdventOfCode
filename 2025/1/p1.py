d = 50
p = 0
for l in open(p):
    d += int(l[1:])*(-1)**(l < 'R')
    d %= 100
    p += d < 1
print(p)
