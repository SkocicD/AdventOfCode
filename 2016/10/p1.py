from collections import defaultdict


def insert_in_order(l, val):
    if len(l) == 0:
        l.append(val)
    else:
        if val > l[0]:
            l.append(val)
        else:
            l.insert(0, val)
    return len(l) == 2


lines = list(l.strip() for l in open(0))
bots = defaultdict(list)
instructions = {}
q = []
outputs = defaultdict(list)
for line in lines:
    inp = {}
    keys = line.split()
    if 'value' == keys[0]:
        bot = int(keys[-1])
        val = int(keys[1])
        if insert_in_order(bots[bot], val):
            q.append(bot)

    else:
        frm = int(keys[1])
        high = (keys[3] == 'high')
        isbot1 = (keys[5] == 'bot')
        to1 = int(keys[6])
        isbot2 = (keys[-2] == 'bot')
        to2 = int(keys[11])
        if not high:
            instructions[frm] = [isbot1, to1, isbot2, to2]
        else:
            instructions[frm] = [isbot2, to2, isbot1, to1]

while q:
    bot = q.pop(0)
    if 61 in bots[bot] and 17 in bots[bot]:
        print(bot)
        exit()
    isbot1, to1, isbot2, to2 = instructions[bot]
    if isbot1:
        if insert_in_order(bots[to1], min(bots[bot])):
            q.append(to1)
    else:
        outputs[to1].append(min(bots[bot]))

    if isbot2:
        if insert_in_order(bots[to2], max(bots[bot])):
            q.append(to2)
    else:
        outputs[to2].append(max(bots[bot]))
