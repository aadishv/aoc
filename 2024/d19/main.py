""" gemini-genned comments
# Grid

*   **`__init__(self, string, delimiter, mapfn, pad=False)`:** Initializes a 2D grid from a string, using a delimiter to split cells and applying a mapping function to each cell, with optional padding.
*   **`window(self, x, y, width, height)`:** Returns a subgrid (window) of the specified dimensions starting at the given coordinates.
*   **`column(self, n)`:** Returns the nth column of the grid.
*   **`row(self, n)`:** Returns the nth row of the grid.
*   **`convolution(self, width, height)`:** Returns a list of all possible subgrids (windows) of the specified dimensions within the grid.

# List Functions

*   **`list_diff(x)`:** Returns a list of the differences between consecutive elements in the input list.
*   **`list_range(x)`:** Returns a list of integers from 0 to x-1.
*   **`lmap(func, *iterables)`:** Applies the given function to each element of the iterable(s) and returns a list of the results.

# Miscellaneous

*   **`ints(s: str) -> typing.List[int]`:** Extracts all integers from a string and returns them as a list.
*   **`regular_process(inp)`:** Cleans up an input string by removing empty lines and leading/trailing whitespace, returning a list of non-empty lines.¸
*   **`factorial(n)`:** Pretty self-explanatory
*   **`bit_not(n, numbits=16)`:** Bitwise not for n-bit number
*   **`list_subtract(l1, l2)`:** Not the most optimized, but subtracts two lists (better than subtracting sets bc it accounts for duped elements)
****

max/min(inp, key=...)
sorted(iterator, key=...) (can use functools.cmp_to_key())
reversed(iterator)
reduced(function, iterator, initial)
itertools.permutations(iterator)
partitions(n [size of total], k [number])
"""
from utils import *
from copy import deepcopy
def list_list_unique(l):
    return list(map(list, set(map(tuple, l))))
def list_string_sum(l):
    return reduce(lambda x, y: x + y, l)
def check(target, patterns):
    dp = [True] + [False] * len(target)

    for i in range(len(target) + 1):
        if not dp[i]:
            continue
        for pattern in patterns:
            if i + len(pattern) <= len(target) and target[i:i+len(pattern)] == pattern:
                dp[i + len(pattern)] = True

    return dp[-1]

def part1(sample):
    patterns, targets = sample.split('\n\n')
    patterns = patterns.split(', ')
    targets = regular_process(targets)
    total = sum([check(i, patterns) for i in targets])
    print(total)
    return

def check2(target, patterns):
    dp = [1] + [0] * len(target)

    for i in range(len(target) + 1):
        if not dp[i]:
            continue
        for pattern in patterns:
            if i + len(pattern) <= len(target) and target[i:i+len(pattern)] == pattern:
                dp[i + len(pattern)] += dp[i]

    return dp[-1]
def part2(sample):
    patterns, targets = sample.split('\n\n')
    patterns = patterns.split(', ')
    targets = regular_process(targets)
    print(sum([check2(t, patterns) for t in targets]))
    return

part = 2
flag = 'i'
SAMPLE = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""


if flag == 's':
    if part == 2:
        part2(SAMPLE)
    else:
        part1(SAMPLE)
if flag == 'i':
    if part == 2:
        part2(tester.INPUT)
    else:
        part1(tester.INPUT)
