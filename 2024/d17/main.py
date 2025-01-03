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
from utils import *
from copy import deepcopy

def test_a(ma, mb, mc, program):
    a, b, c = deepcopy(ma), deepcopy(mb), deepcopy(mc)
    output = []
    while a != 0:
        # b is not dependent on previous iterations
        # thus the "ticker" is just a getting divided by 8
        b = (a & 7) ^ 2
        b = (b ^ (a//(1 << b))) ^ 3
        a = a >> 3
        output.append(b%8)
    return output
def part1(sample):
    registers, program = sample.split('\n\n')
    a, b, c = ints(registers)
    program = ints(program)

    print(test_a(a, b, c, program))
    return

def part2(sample):
    registers, program = sample.split('\n\n')
    program = ints(program)

    mya = 1 # maximum that has length 16
    matching = -1

    while matching != -16:
        output = test_a(mya, 0, 0, program)
        if output[matching:] == program[matching:]:
            print(mya, output)
            mya *= 8
            matching -= 1
        mya += 1
    print(mya, test_a(mya, 0, 0, program) == program, matching)
    time.sleep(2)
    return

part = 2
flag = 'i'
SAMPLE = """Register A: 117440
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
"""


if flag == 's':
    if part == 2:
        part2(SAMPLE)
    else:
        part1(SAMPLE)
if flag == 'i':
    if part == 2:
        part2(tester.INPUT)
    else:
        part1(tester.INPUT)
