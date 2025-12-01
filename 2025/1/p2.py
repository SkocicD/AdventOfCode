import sys
dial = 50
password = 0
for line in sys.stdin:
    s = (line[0] == "L")
    prev = dial
    dial += int(line[1:]) * (-1)**s
    password += abs(int(dial / 100))
    if dial <= 0 and prev != 0:
        password += 1
    print(dial, password)
    dial %= 100
print(password)
