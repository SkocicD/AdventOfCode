stones = list(map(int, input().split()))

for blink in range(25):
    next = []
    for stone in stones:
        if stone == 0:
            next.append(1)
        elif len(s := str(stone)) % 2 == 0:
            next.append(int(s[:int(len(s)/2)]))
            next.append(int(s[int(len(s)/2):]))
        else:
            next.append(2024*stone)
    stones = next
print(len(stones))
