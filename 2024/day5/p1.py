from collections import defaultdict
lines = open('input.txt','r').read()
lines = lines.split('\n')[:-1]

before = defaultdict(set)
after = defaultdict(set)

i = 0
while '|' in (line:=lines[i]):
    left = int(line[0:line.index('|')])
    right = int(line[line.index('|')+1:])
    before[right].add(left)
    after[left].add(right)
    i+=1

i+=1
total = 0
while i < len(lines):
    line=lines[i]
    lineBefore = []
    correct = True
    for num in (nums:=list(map(int, line.split(',')))):
        for prev in lineBefore:
            if num not in after[prev]:
                correct = False
                break
        lineBefore.append(num)
        if not correct:
            break
    else:
        total += nums[len(nums)//2]
    i+=1

print(total)