lines = open('input2.txt','r').read()
lines = lines.split('\n')[:-1]

def check(goal, curr, nums):
    if len(nums) == 0:
        return curr == goal

    if curr <= goal:
        return check(goal, curr+nums[0], nums[1:]) or check(goal, curr*nums[0], nums[1:]) or check(goal, int(str(curr) + str(nums[0])), nums[1:])

    return False

total = 0

for i, line in enumerate(lines):

    goal = int(line[:line.index(':')])
    line = line[line.index(':') + 1:]
    nums = list(map(int, line.split()))

    if check(goal,nums[0], nums[1:]):
        total += goal

print(total)
