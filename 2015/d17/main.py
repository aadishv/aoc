from uuid import uuid4
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
reduce(function, iterator, initial)
itertools.permutations(iterator)
partitions(n [size of total], k [number])
"""

def solve(sample) -> int:
    TOTAL = 150
    bottles = ints(sample)
    bottles = [(i, random.random()) for i in bottles]
    queue = [[i] for i in bottles]
    n=0
    while not all([sum([j[0] for j in i]) == TOTAL for i in queue]):
        print("growing stage", n, len(queue))
        n += 1
        newq = []
        for i in queue:
            for j in list_subtract(bottles, i):
                if sum([z[0] for z in i+[j]]) <= TOTAL:
                    newq.append(i+[j])
            if sum([z[0] for z in i]) == TOTAL:
                newq.append(i)
        queue = newq
    queue = [set(j) for j in set([tuple(sorted(i)) for i in queue])]
    queue = [[i[0] for i in j] for j in queue]
    minimum_number = min([len(i) for i in queue])
    print(len([i for i in queue if len(i) == minimum_number]))




    return 0


SAMPLE = """
"""
print(solve(tester.INPUT))
