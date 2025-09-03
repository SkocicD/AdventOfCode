s = input()
sum = 0

spaces = list(map(int, s[1::2]))
numbers = list(map(int, s[0::2]))

l = 0
r = len(numbers)
index = 0
space = 0
endcounter = 0

while l < r:
    for j in range(numbers[l]):
        sum += index * l
        index += 1

    for j in range(spaces[l]):
        if endcounter == 0:
            r -= 1
            if r <= l:
                break
            endcounter = numbers[r]
        sum += index * r
        index += 1
        endcounter -= 1

    l += 1

while endcounter > 0:
    sum += index * r
    index += 1
    endcounter -= 1

print(sum)
