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

alphabet = list('abcdefghijklmnoqrstuvwxyz')
def increment(sample) -> str:
    if sample[-1] == 'z':
        return increment(sample[:-1])+'a'
    else:
        return sample[:-1]+alphabet[alphabet.index(sample[-1])+1]
def check_if_sample_good(sample) -> str:
    if sample == "hxbxxyzz":
        return False
    for i in ['i', 'o', 'l']:
        if i in sample:
            return False

    contains_3_string = False
    for i in range(23):
        if ''.join(alphabet[i:i+3]) in sample:
            contains_3_string = True
    if not contains_3_string:
        return False

    n_double_repeats = 0
    for i in alphabet:
        if i+i in sample:
            n_double_repeats += 1
    if n_double_repeats < 2:
        return False
    return True
def solve(sample) -> int:
    output = 0
    while not check_if_sample_good(sample):
        if sample == "ghjaabcc":
            print("fgd")
        sample = increment(sample)
    print(sample)

    return sample


SAMPLE = "ghijklmn"
print("Solving")
print(solve("hxbxxyzz"))
