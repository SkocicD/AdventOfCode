import sys
dial = 50
password = 0
for line in sys.stdin:
    s = (line[0] == "L")
    dial = (dial + int(line[1:]) * (-1)**s) % 100
    if not dial:
        password += 1
print(password)
