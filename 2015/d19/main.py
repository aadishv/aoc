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

def indexes(l, match):
    return [i for i in range(len(l)) if l[i:i+len(match)] == match]

def solve(sample) -> int:
    lines = regular_process(sample)
    rules = '\n'.join(lines[:-1])
    elements = set(re.findall(r'[A-Z][a-z]?', ))
    print(list(set())
    output = 0


    rules =
    rules = sorted(rules, key=lambda x: len(x[0]), reverse=True)
    #rules = [(r[1], r[0]) for r in rules]
    initial_molecule = lines[-1]

    queue = {'e'}
    n = 0
    while True:
        print(n, len(queue))
        n += 1
        newq = set()
        for i in queue:
            for rule in [r for r in rules if r[0] in i]:
                r0 = rule[0]
                r1 = rule[1]
                lr0 = len(rule[0])
                lr1 = len(rule[1])
                for ind in indexes(i, r0):
                    new = i[:ind] + r1 + i[ind + lr0:]
                    if new == initial_molecule:
                        return time + 1
                    if len(new) < len(initial_molecule):
                        newq.add(new)
        queue = newq

    return 0


SAMPLE = """e => H
e => O
H => HO
H => OH
O => HH
HOHOHO
"""
flag = 'i'
if flag == 's':
    print(solve(SAMPLE))
if flag == 'i':
    print(solve(tester.INPUT))
