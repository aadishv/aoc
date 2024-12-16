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
from collections import deque

def part1(sample):
    grid = Grid.from_string(sample)
    start = grid.index('S')
    end = grid.index('E')
    queue = deque([(start, V(1, 0), 0, [start])])  # pos, dir, score, points
    visited = {}

    final = []
    while queue:
        print(len(queue))
        pos, dir, score, points = queue.popleft()

        if pos == end:
            final.append((score, points))
            continue
        if (pos, dir) in visited and visited[(pos, dir)] < score:
            continue
        else:
            visited[(pos, dir)] = score

        for d in V.CARDINAL_DIRECTIONS:
            # Check if it's a turn (vectors are perpendicular)
            is_turn = (dir[0] * d[0] + dir[1] * d[1]) == 0 and d != dir
            diff = 1000 if is_turn else 0

            new_pos = pos + d
            if new_pos not in grid:
                continue
            if grid[new_pos] in '.E':
                queue.append((new_pos, d, score + diff + 1, points + [new_pos]))
    m = min(final, key=lambda x: x[0])[0]
    points = flatten([i[1] for i in final if i[0] == m])
    for p in points:
        grid[p] = 'O'
    print('Part 1:', m)
    print('Part 2:', len(set(points)))
    exit()

part = 1
flag = 'i'
SAMPLE = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""

"""#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
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
