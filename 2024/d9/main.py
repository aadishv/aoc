








import sys
sys.path.append('../../')
from utils import *
from copy import deepcopy
import re

sample = """2333133121414131402"""
inp = open('input.txt').read()

pieces = []
n = 0
a = True
for b in list(inp):
    if a:
        pieces += [str(n)]*int(b)
        n += 1
    else:
        pieces += ['.']*int(b)
    a = not a
if len(sample) % 2 == 1:
    if pieces[-1] == '.':
        pieces += [str(n)] * int(sample[-1])
    else:
        pieces += ['.'] * int(sample[-1])

while not re.fullmatch(r'(\d+)(\.+)', ''.join(pieces)):
    nextt = [i for i in range(len(pieces)) if pieces[i] == '.'][0]
    next = [i for i in range(len(pieces)) if pieces[i] != '.'][-1]
    pieces[nextt] = pieces[next]
    pieces[next] = '.'
s = 0
for i, v in enumerate(pieces):
    if v == '.':
        continue
    #print(i, v)
    s += int(v)*i
print(s)
