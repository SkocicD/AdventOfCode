lines = open('input.txt','r').read()
lines = lines.split('\n')[:-1]

def check(goal, nums):
    if goal == 0 or len(nums) == 0:
        return (len(nums) == goal)

    if nums[-1] <= goal:
        mult = False
        if goal % nums[-1] == 0:
            mult = check(goal//nums[-1], nums[:-1])
        add = check(goal-nums[-1], nums[:-1])
        return mult or add
    return False


total = 0

for i, line in enumerate(lines):

    goal = int(line[:line.index(':')])
    line = line[line.index(':') + 1:]
    nums = list(map(int, line.split()))

    if check(goal,nums):
        total += goal

print(total)
