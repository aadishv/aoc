# modified from `../d2/main.py`
import sys
from copy import deepcopy
from utils import *
import itertools
inp = sys.stdin.read()
sample = """3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99
"""
s = sample
ss = ints(inp)

s = deepcopy(ss)

input = [5]
output = []

p = 0
print(s[:50])
while p < len(s):
    print(p)
    opcode = int(str(s[p])[-2:])
    def param(n):
        modes = list(reversed(str(s[p])[:-2]))
        parammode = 0
        if n-1 in range(len(modes)):
            parammode = int(modes[n-1])
        if parammode == 0:
            return s[s[p+n]]
        elif parammode == 1:
            return s[p+n]
    if opcode == 1:
        print(opcode, p)
        s[s[p+3]] = param(1)+param(2)
        p += 4
    elif opcode == 2:
        s[s[p+3]] = param(1)*param(2)
        p += 4
    elif opcode == 3:
        v = input.pop(0)
        s[s[p+1]] = v
        p += 2
    elif opcode == 4:
        output.append(param(1))
        p += 2
    elif opcode == 5:
        if param(1) != 0:
            p = param(2)
        else:
            p += 3
    elif opcode == 6:
        if param(1) == 0:
            p = param(2)
        else:
            p += 3
    elif opcode == 7:
        if param(1) < param(2):
            s[s[p+3]] = 1
        else:
            s[s[p+3]] = 0
        p += 4
    elif opcode == 8:
        if param(1) == param(2):
            s[s[p+3]] = 1
        else:
            s[s[p+3]] = 0
        p += 4
    elif opcode == 99:
        break
print(output)
