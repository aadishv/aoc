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
from test.test_heapq import R

def solve(sample) -> int:
    output = 0
    rules = []
    things = []
    lines = regular_process(sample)
    for l in lines:
        if l != '':
            if '|' in l:
                rules.append([int(i) for i in l.split('|')])
            else:
                things.append([int(i) for i in l.split(',')])
    def check_thing(thing):
        works = True
        for t in range(len(thing)):
            tt = thing[t]
            for i in range(t+1, len(thing)):
                if not [tt, thing[i]] in rules:
                    works = False
        return works
    for thing in things:
        works = check_thing(thing)
        if works:
            pass # output += thing[len(thing)//2]
        else:
            for t in range(len(thing)):
                for i in range(t+1, len(thing)):
                    if [thing[i], thing[t]] in rules: # reversed
                        thing[i], thing[t] = thing[t], thing[i]

            output += thing[len(thing)//2]
    return output


SAMPLE = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""
print(solve(tester.INPUT))
