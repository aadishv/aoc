import sys
from copy import deepcopy
from utils import *

inp = sys.stdin.read()
sample = inp
"""3   4
4   3
2   5
1   3
3   9
3   3"""
x = lmap(ints, sample.split('\n'))
x = lmap(lambda i: sorted([a[i] for a in x]), [0, 1])
x = sum([abs(a-b) for a, b in list(zip(*x))])
print(x)



y = lmap(ints, sample.split('\n'))
y = lmap(lambda i: [a[i] for a in y], [0, 1])
y = sum(lmap(lambda a: a*y[1].count(a), y[0]))
print(y)
