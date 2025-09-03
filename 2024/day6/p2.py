area = open('input.txt','r').read()
area = area.split('\n')[:-1]

def inBounds(p):
    return (0 <= p.r and p.r < len(area) and 0 <= p.c and p.c < len(area[0]))

class Position:
    def __init__(self, r, c, dir='up'):
        self.r = r
        self.c = c
        self.dir = dir

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

    def __eq__(self, other):
        if not isinstance(other, Position):
            return False
        return self.r == other.r and self.c == other.c and self.dir == other.dir

    def __hash__(self):
        return hash((self.r, self.c, self.dir))

    def __str__(self):
        return '(' + str(self.r) + ', ' + str(self.c) + ') facing ' + self.dir


for r in range(len(area)):
    for c in range(len(area[r])):
        if area[r][c] == '^':
            startPos = Position(r,c,'up')

positions = set()

pos = Position(startPos.r, startPos.c)

while inBounds(pos):
    positions.add(Position(pos.r, pos.c, 'up'))
    while True:
        r, c = pos.next() 
        if inBounds(Position(r,c,'up')) and area[r][c] == '#':
            pos.toggleDir()
        else:
            break
    pos.step()

loopers = 0
for p in positions:
    area[p.r] = area[p.r][:p.c] + '#' + area[p.r][p.c+1:]

    orientations = set()
    pos = Position(startPos.r, startPos.c)

    while inBounds(pos):
        sizeBefore = len(orientations)
        orientations.add(Position(pos.r, pos.c, pos.dir))
        if sizeBefore == len(orientations):
            loopers += 1
            break
        while True:
            r, c = pos.next() 
            if inBounds(Position(r,c,'up')) and area[r][c] == '#':
                pos.toggleDir()
            else:
                break
        pos.step()

    area[p.r] = area[p.r][:p.c] + '.' + area[p.r][p.c+1:]

print(loopers)
