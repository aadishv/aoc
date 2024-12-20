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

def part1(sample):
    instructions = regular_process(sample)
    registers = {'a': 1, 'b': 0}
    i = 0
    while i < len(instructions):
        instr = instructions[i]
        r = split_mult(instr, ' ,')[1]
        if instr == 'jmp -7':
            print('fffff')
        moved = False
        match instr[:3]:
            case 'hlf':
                registers[r] = int(0.5 * registers[r])
            case 'tpl':
                registers[r] = 3 * registers[r]
            case 'inc':
                registers[r] += 1
            case 'jmp':
                i += int(r)
                moved = True
            case 'jie':
                if registers[r] % 2 == 0:
                    i += int(split_mult(instr, ' ,')[2])
                    moved = True
            case 'jio':
                if instr == "jio a, +8":
                    print(registers)
                if registers[r] == 1:
                    i += int(split_mult(instr, ' ,')[2])
                    moved = True
        if not moved:
            i += 1
        print(i)
    print(registers)
    return
def part2(sample):

    return


part = 1
flag = 'i'
SAMPLE = """inc a
jio a, +2
tpl a
inc a"""


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
