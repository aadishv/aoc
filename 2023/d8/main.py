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
import re

def part1(sample):
    instructions, map = sample.split('\n\n')
    map = re.findall(r'(\w+) = \((\w+), (\w+)\)', map)
    node = 'AAA'
    n = 0
    p = 0
    while True:
        if node == 'ZZZ':
            print(n)
            break
        else:
            if instructions[p] == 'L':
                node = [m for m in map if m[0] == node][0][1]
            else:
                node = [m for m in map if m[0] == node][0][2]
            p += 1
            p = p % len(instructions)
        n += 1


    return
def part2(sample):
    instructions, map = sample.split('\n\n')
    map = re.findall(r'(\w+) = \((\w+), (\w+)\)', map)
    newmap = {}
    for m in map:
        newmap[(m[0], 'L')] = m[1]
        newmap[(m[0], 'R')] = m[2]


    nodes = [i[0] for i in map if i[0][-1] == 'A']

    for node in nodes:
        l = [node]
        p = 0
        while len(l) == 1 or l[-1][-1] != 'A':
            print(l)
            l.append(newmap[(l[-1], instructions[p])])
            p = (p+1) % len(instructions)
        print(l)
    return

part = 2
flag = 's'
SAMPLE = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
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
