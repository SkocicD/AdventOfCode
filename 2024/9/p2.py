s = list(map(int, input()))
sum = 0

spaces = list(map(int, s[1::2]))
numbers = list(map(int, s[0::2]))
indices = {}
index = 0
for i, n in enumerate(s):
    indices[i] = index
    index += n

print(indices)

# iterate over files backwards
for i, num in list(enumerate(s))[::-2]:
    # iterate over spaces before the file
    for j in range(len(s))[1:i:2]:
        if num <= s[j]:
            # print(f"found that file {i//2} can move to space {j//2}")
            indices[i] = indices[j]
            s[j] -= num
            indices[j] += num
            break

sum = 0
for i, num in list(enumerate(s))[::2]:
    index = indices[i]
    for j in range(num):
        sum += index * i//2
        index += 1

print(sum)
