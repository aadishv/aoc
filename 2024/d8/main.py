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
import itertools
def solve(sample) -> int:

    output = 0
    antennas = []
    grid = Grid(sample, '', lambda x: x)
    for i in grid.all_coordinates():
        if grid.at(*i) not in ['.', '#']:
            antennas.append((i, grid.at(*i)))
    # go thru pairs of antennas with same freq
    ta = []
    for i, j in itertools.product(antennas, repeat=2):
        if i[1] == j[1]:
            # check if they're in the same line
            if i[1] == j[1]:
                # antinodes
                difference = (i[0][0] - j[0][0], i[0][1] - j[0][1])
                for x in range(-100, 100):
                    ta.append(Grid.vector_add(Grid.vector_multiply(difference, x), i[0]))
    ta = [c for c in ta if c in grid.all_coordinates()]
    for c in ta:
        grid.set(*c, '#')
    print('\n'.join([''.join(i) for i in grid.grid]))
    print(len(grid.all_coordinates())-grid.count('.'))
    return


SAMPLE = """##....#....#
.#.#....0...
..#.#0....#.
..##...0....
....0....#..
.#...#A....#
...#..#.....
#....#.#....
..#.....A...
....#....A..
.#........#.
...#......##
"""
flag = 'i'
if flag == 's':
    print(solve(SAMPLE))
if flag == 'i':
    print(solve(tester.INPUT))
