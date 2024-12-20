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
import itertools

def get_all_target(pckgs, t):
    queue = [[i] for i in deepcopy(pckgs)]
    final = []
    while queue != []:
        print('getting', len(queue), min(map(len, queue)), max(map(len, queue)), final, t)
        pckg = queue.pop(0)

        for n in list_subtract(pckgs, pckg):
            new = pckg + [n]
            news = sum(new)
            if news < t:
                queue.append(new)
            elif news == t:
                final.append(new)
    return final

def part1(sample):
    packages = ints(sample)
    weight = sum(packages)//3
    options = set()
    l = len(packages)
    r = get_all_target(packages, weight)
    f_l = min(map(len, r))
    best = (None, [])
    n = 0
    for a, b in itertools.product(r, repeat=2):
        print(n)
        n += 1
        if unique(a+b) == a+b and len(a) == f_l:
            qe = product(a)
            if best[0] == None or qe < best[0]:
                best = (qe, a)
            # c = list(list_subtract(packages, a+b))
            # t = tuple(map(tuple, [a, b, c]))
            # options.add(t)
    print(qe)
    return
def part2(sample):

    return

part = 1
flag = 'i'
SAMPLE = """"1
2
3
4
5
7
8
9
10
11"""


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
