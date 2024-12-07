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



def solve(sample) -> int:
    lines = regular_process(sample)
    grid = Grid(sample, '', str, pad=True)
    for i in [0, grid.width-1]:
        for j in [0, grid.height-1]:
            grid.grid[j][i] = '#'
    for _ in range(100):
        newgrid = deepcopy(grid)
        for y in range(grid.height):
            for x in range(grid.width):
                total = sum([1 for r in grid.neighbors(x, y) if grid.grid[r[1]][r[0]] == '#'])
                if grid.grid[y][x] == '.':
                    if total == 3:
                        newgrid.grid[y][x] = '#'
                else:
                    if total not in [2, 3]:
                        newgrid.grid[y][x] = '.'
        for i in [0, grid.width-1]:
            for j in [0, grid.height-1]:
                newgrid.grid[j][i] = '#'
        grid = newgrid
    print(('\n'.join([''.join(i) for i in newgrid.grid])).count('#'))
    return 0


SAMPLE = """.#.#.#
...##.
#....#
..#...
#.#..#
####..
"""
print(solve(tester.INPUT))
