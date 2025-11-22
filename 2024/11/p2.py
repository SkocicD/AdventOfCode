# This one was a fun one
stones = list(map(int, input().split()))
already_seen = {}


def test(stone, blinks_left):
    global already_seen

    if blinks_left == 0:
        return 1
    if (stone, blinks_left) in already_seen:
        return already_seen[(stone, blinks_left)]

    total = 0
    if stone == 0:
        total += test(1, blinks_left-1)
    elif len(s := str(stone)) % 2 == 0:
        total += test(int(s[:int(len(s)/2)]), blinks_left-1)
        total += test(int(s[int(len(s)/2):]), blinks_left-1)
    else:
        total += test(2024*stone, blinks_left-1)
    already_seen[(stone, blinks_left)] = total
    return total


total = 0
for stone in stones:
    total += test(stone, 75)

print(total)
