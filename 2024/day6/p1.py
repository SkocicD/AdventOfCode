area = open('input.txt','r').read()
area = area.split('\n')[:-1]

def inBounds(p):
    return (0 <= p.r and p.r < len(area) and 0 <= p.c and p.c<=len(area[0]))

class position:
    def __init__(self, r,c):
        self.r = r
        self.c = c
        self.dir = 'up'

    def toggleDir(self):
        if self.dir == 'up':
            self.dir = 'right'
        elif self.dir == 'right':
            self.dir = 'down'
        elif self.dir == 'down':
            self.dir = 'left'
        elif self.dir == 'left':
            self.dir = 'up'

    def step(self):
        if self.dir == 'up':
            self.r -= 1
        elif self.dir == 'right':
            self.c += 1
        elif self.dir == 'down':
            self.r += 1
        elif self.dir == 'left':
            self.c -= 1

    def next(self):
        currr = self.r
        currc = self.c
        self.step()
        r = self.r
        c = self.c
        self.r = currr
        self.c = currc
        return (r, c)

for r in range(len(area)):
    for c in range(len(area[r])):
        if area[r][c] == '^':
            pos = position(r,c)

positions = set()

steps = 0
while inBounds(pos):
    positions.add((pos.r, pos.c))
    while True:
        r, c = pos.next() 
        if inBounds(position(r,c)) and area[r][c] == '#':
            pos.toggleDir()
        else:
            break
    pos.step()

print(len(positions))
