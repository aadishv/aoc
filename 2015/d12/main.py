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
****

max/min(inp, key=...)
sorted(iterator, key=...) (can use functools.cmp_to_key())
reversed(iterator)
reduced(function, iterator, initial)
"""


def check(obj) -> int:
    if isinstance(obj, int):
        return obj
    if isinstance(obj, str):
        return 0
    if isinstance(obj, list):
        return reduce(lambda a,b: a+b, [check(o) for o in obj], 0)
    if isinstance(obj, dict):
        if 'red' in list(obj.values()):
            return 0
        return reduce(lambda a,b: a+b, [check(o) for o in list(obj.values())], 0)
def solve(sample) -> int:
    output = 0

    loaded = json.loads(sample)
    print(check(loaded))
    return output


SAMPLE = """[1,{"c":"red","b":2},3]"""
print(solve(tester.INPUT))
