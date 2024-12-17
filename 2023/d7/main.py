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
from functools import cmp_to_key

def part1(sample):
    def rank(a):
        cons = sorted(length_consecutive(sorted(a)))
        if cons == [5]: # five of a kind
            return 1
        elif cons == [1, 4]: # four of a kind
            return 2
        elif cons == [2, 3]: # full houes
            return 2.5
        elif cons == [1, 1, 3]: # three of a kind
            return 3
        elif cons == [1, 2, 2]: # two pairs
           return 4
        elif cons == [1, 1, 1, 2]: # one pair
           return 5
        elif cons == [1]*5: # high card
           return 6
        print(a, cons)
    decks = [(i.split()[0], int(i.split()[1])) for i in sample.split('\n') if i != '']
    values = sorted([(d, 6-rank(d[0])) for d in decks], key=lambda v: v[1])
    values = sorted(
        runs(values, lambda l: all([i[-1] == l[0][-1] for i in l])),
        key=lambda v: v[-1][-1]
    )
    for run in values:
        print(run)
    return
def part2(sample):

    return

part = 1
flag = 's'
SAMPLE = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""


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
