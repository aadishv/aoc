import sys
from copy import deepcopy
from utils import *

inp = sys.stdin.read()
sample = """"""
n = 0
for option in range(193651, 649729):
    digits = lmap(int, list(str(option)))
    if 2 in lmap(len, runs(digits)):
        if all(i >= 0 for i in list_diff(digits)):
            n += 1
print(n)
