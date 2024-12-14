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
from collections import defaultdict

def part1(sample):
    w = 101
    h = 103
    robots = []
    for l in regular_process(sample):
        px, py, vx, vy = ints(l)
        for i in range(100):
            px += vx
            py += vy
            # wrap around - width is 101, height is 103
            px = (px + w*2)%w
            py = (py + h*2)%h
        robots.append((px, py))
    quadrants = defaultdict(list)
    for robot in robots:
        ww = False if robot[0] < w/2-1 else True if robot[0] > w/2 else None
        hh = False if robot[1] < h/2-1 else True if robot[1] > h/2 else None
        quadrants[(ww, hh)].append(robot)
    keys = [(True, True), (True, False), (False, True), (False, False)]
    return
def part2(sample):
    w = 101
    h = 103
    txt = ''
    robots = []
    for l in regular_process(sample):
        ls = []
        px, py, vx, vy = ints(l)
        for i in range(10000):
            px += vx
            py += vy
            # wrap around - width is 101, height is 103
            px = (px + w*2)%w
            py = (py + h*2)%h
            ls.append((px, py))
        robots.append(ls)
    for i in range(10000):
        rs = [robot[i] for robot in robots]
        if len(rs) == len(set(rs)):
            r = [['.' if (x, y) not in rs else '*' for x in range(w)] for y in range(h)]
            print('\n'.join([''.join(i) for i in r]))
    open('output.txt', 'w').write(txt)
    return


part = 2
flag = 'i'
SAMPLE = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""


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
exit()
