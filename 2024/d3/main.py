import sys
sys.path.append('../../')
from utils import *
from copy import deepcopy
import re

sample = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
inp = open('input.txt').read()

s = inp
t = 343440
g = True
for i in re.findall(r'(mul\(\d+,\d+\)|do\(\)|don\'t\(\))', s):
    if 'don' in i:
        g = False
    elif 'do' in i:
        g = True
    else:
        if g:
            t += product(ints(i))
print(t)
