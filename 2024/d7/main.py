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
itertools.product([options...], repeat=times...) # get all permutations of a set of values repeated n times
"""



def solve(sample) -> int:
    output = 0

    lines = regular_process(sample)
    for l in lines:
        target = ints(l)[0]
        values = ints(l)[1:]
        for combo in itertools.product([0, 1, 2], repeat=len(values)-1):
            e = values[0]
            for i in range(len(combo)):
                if combo[i] == 1:
                    e *= values[i+1]
                elif combo[i] == 2:
                    e = int(str(e) + str(values[i+1]))
                else:
                    e += values[i+1]
            if e == target:
                output += target
                break
    return output


SAMPLE = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""
flag = 'i'
if flag == 's':
    print(solve(SAMPLE))
if flag == 'i':
    print(solve(tester.INPUT))
