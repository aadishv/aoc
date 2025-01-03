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
itertools.permutations(iterator)
partitions(n [size of total], k [number])
"""



def solve(sample) -> int:
    RESULTS = ["children: 3", "cats: 7", "samoyeds: 2", "pomeranians: 3", "akitas: 0", "vizslas: 0", "goldfish: 5", "trees: 3", "cars: 2", "perfumes: 1"]
    grandmas = re.findall(r'Sue (\d+): ((\w+: \d+(,\s|\s))+)', sample)
    grandmas = [(g[0], g[1].strip().split(', ')) for g in grandmas]

    best = (-1, 0)
    for g in grandmas:
        actual_g = [
            f for f in g[1] if not any(
                [i in f for i in ['cats', 'trees', 'pomeranians', 'goldfish']]
            )
        ]
        relatedness = len(list(set(actual_g).intersection(set(RESULTS))))
        print(relatedness, end = " ")
        for i in ['cats', 'trees']:
            result_one = ints([r for r in RESULTS if i in r][0])[0]
            this_grandma = [r for r in g[1] if i in r]
            if this_grandma != []:
                this_grandma = ints(this_grandma[0])[0]
                if this_grandma > result_one:
                    relatedness += 1
        for i in ['pomeranians', 'goldfish']:
            result_one = ints([r for r in RESULTS if i in r][0])[0]
            this_grandma = [r for r in g[1] if i in r]
            if this_grandma != []:
                this_grandma = ints(this_grandma[0])[0]
                if this_grandma < result_one:
                    relatedness += 1
        print(relatedness)
        if relatedness > best[1]:
            best = (g[0], relatedness)
    print(best)
    return 0


SAMPLE = """
"""
print(solve(tester.INPUT))
