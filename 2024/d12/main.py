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

def part1(sample):
    regions = []
    grid = Grid(sample)
    a = grid.all_coordinates()
    # kinda like a flood fill
    while a != []:
        q = [a.pop(0)]
        x = grid.at(q[0])
        done = False
        newq = []
        rd = False
        lastq = []
        while True:
            lastq = deepcopy(q)
            rd = False

            for i in q:
                for n in grid.straight_neighbors(i):
                    if n in a and grid.at(n) == x:
                        q.append(n)
                        a.remove(n)
                        rd = True
            if not rd:
                break
        regions.append((q, x))

    cost = 0
    for region in regions:#[j for j in regions if j[1] == 'C']:
        corners = []
        for p in region[0]:
            # get all points
            for i in range(len(grid.CARDINAL_DIRECTIONS)):
                c = Grid.vector_add(p, grid.CARDINAL_DIRECTIONS[i])
                if not grid.in_bounds(c) or grid.at(c) != region[1]:
                    corners.append((c, grid.CARDINAL_DIRECTIONS[(i+1)%4]))
        # remove corners with the same direction and offset
        corners = list(set(corners))
        newcorners = deepcopy(corners)
        #print([i[0] for i in corners])
        p = len(corners)
        #print([i[0] for i in corners])
        for corner in corners:
            next = corner[0]
            while True:
                next = Grid.vector_add(next, corner[1])

                # if corner[0] in [(0,3), (1,3)]:
                #         print(corner, next)
                if (next, corner[1]) in corners:
                    if (next, corner[1]) in newcorners: # check if it's alr been removed
                        newcorners.remove((next, corner[1]))
                else:
                    break
        #xsprint(len(newcorners), region[1])
        #print([i[0] for i in newcorners])
        cost += len(newcorners) * len(region[0])
    print(cost)
    return

part = 1
flag = 'i'
SAMPLE = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
""".strip()

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
