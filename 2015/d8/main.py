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
****
    def bit_not(n, numbits=16):
            return (1 << numbits) - 1 - n
"""
def solve(sample) -> int:
    output = 0
    lines = regular_process(sample)
    total = 0
    at = 0
    mapping = {'"': 2, '\\': 2}
    for l in lines:
        total += len(l)
        at += len(l) + 2
        matches = re.findall(r"""(\"|\\|\\x\w{2})""", l)
        at += len(matches)
        #print(matches)
        print(len(l)+len(matches))
        # split = ['', l[1:-1]]
        #
        # matches_l = functools.reduce(lambda a, b: a + len(b), matches, 0)
        # at += len(split[1])-matches_l+len(matches)

    return at - total


SAMPLE = """
""
"abc"
"aaa\\"aaa"
"\\x27"
"""
print(solve(tester.INPUT))
