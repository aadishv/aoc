import sys
from copy import deepcopy
from utils import *
import re
from collections import defaultdict
inp = sys.stdin.read()
SAMPLE = """1
2
3
2024"""

sample = SAMPLE

def mix_prune(v, n):
    return (v ^ n) % 16777216
def get_val_at(v, p):
    val = deepcopy(v)
    # 24-bit integer, as we are modulo by 16777216 (2^24) every operation
    for i in range(p):
        val = mix_prune(val, val*64)
        val = mix_prune(val, val//32)
        val = mix_prune(val, val * 2048)
    return val
def runs(y):
    total = defaultdict(int)
    n = 0
    for val in y:
        print(n, len(y))
        n += 1
        xs = [get_val_at(val, p) % 10 for p in range(2001)]
        seen = set()
        for i in range(0, len(xs)-4):
            p = tuple(list_diff(xs[i:i+5]))
            if p not in seen:
                total[p] += xs[i+4]
            seen.add(p)
    return max(total.values())
print(runs(ints(inp)))
