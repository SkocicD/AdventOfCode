import time
input = open("input.txt",'r').read()

total = 0
enable = True
while True:
    try:
        while True:
            if "do()" in input:
                do = input.index("do()")
            else:
                do = len(input)
            if "don't()" in input:
                dont = input.index("don't()")
            else:
                dont = len(input)
            c = input.index("mul(") + 4
            if do < c or dont < c:
                if do < dont:
                    enable = True
                    input = input[do+4:]
                else:
                    enable = False
                    input = input[dont+7:]
            else:
                break
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
            if enable:
                total += int(n1) * int(n2)
        input = input[c:]
    except ValueError:
        break
print(total)
