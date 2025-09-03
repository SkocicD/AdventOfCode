import time
input = open("input.txt",'r').read()

total = 0
while True:
    try:
        c = input.index("mul(") + 4
        n1 = ''
        n2 = ''
        comma = False
        paren = False
        while not paren:
            if not input[c].isnumeric():
                if not comma and input[c]!=',':
                    break
                elif not comma and input[c]==',':
                    comma = True
                elif not paren and input[c]!=')':
                    break
                elif not paren and input[c]==')':
                    paren = True
            elif comma and not paren:
                n2 += input[c]
            elif not comma and not paren:
                n1 += input[c]
            c += 1
        else:
            if not (len(n1) > 3 or len(n2) > 3):
                total += int(n1) * int(n2)
        input = input[c:]
    except ValueError:
        break
print(total)
