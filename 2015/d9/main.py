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
from test.test_heapq import N


def factorial(n) -> int:
    if n==1:
        return 1
    return n*factorial(n-1)

def solve(sample) -> int:
    output = 0
    lines = regular_process(sample)
    routes = {}
    for l in lines:
        split = l.split()
        routes[tuple(sorted([split[0], split[2]]))] = split[4]
    def check_destinations(a, b):
        if tuple(sorted([a, b])) in list(routes.keys()):
            return routes[tuple(sorted([a, b]))]
        return None
    all_destinations = list(set([r[0] for r in routes] + [r[1] for r in routes]))
    queue = [([d], 0) for d in all_destinations]

    while len(queue[0][0]) != len(all_destinations):
        new_queue = []
        for i in queue:
            for j in all_destinations:
                r = check_destinations(i[0][-1], j)
                if r != None and j not in i[0]:
                    new_queue.append((i[0]+[j], i[1] + int(r)))
        queue = new_queue
    best = max(queue, key=lambda a: a[1])[1]

    return best


SAMPLE = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
"""
print(solve(tester.INPUT))
