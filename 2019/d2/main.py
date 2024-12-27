import sys
from copy import deepcopy
from utils import *
import itertools
inp = sys.stdin.read()
sample = """1,1,1,4,99,5,6,0,99"""
s = inp
ss = ints(s)

for a, b in itertools.product(range(100), range(100)):
    s = deepcopy(ss)
    s[1], s[2] = a, b

    p = 0
    while p < len(s):
        opcode = s[p]
        if opcode == 1:
            s[s[p+3]] = s[s[p+1]]+s[s[p+2]]
        elif opcode == 2:
            s[s[p+3]] = s[s[p+1]]*s[s[p+2]]
        else:
            break
        p += 4
    if s[0] == 19690720:
        print(100*a+b)
