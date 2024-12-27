import sys
from copy import deepcopy
from utils import *

inp = sys.stdin.read()
sample = """"""

n = 0
def calc(n):
    t = 0
    while True:
        n = n // 3 - 2
        if n <= 0:
            break
        t += n

    return t
# print(calc(100756))
print(sum(map(calc, ints(inp))))
