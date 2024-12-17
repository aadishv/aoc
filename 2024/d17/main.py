from pickle import APPENDS
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
from z3 import *

def part1(sample):
    registers, program = sample.split('\n\n')
    registers = ints(registers)

    initial_b, initial_c = registers[1], registers[2]

    program = ints(program)


    def test_a(ma):
        a, b, c = deepcopy(ma), deepcopy(initial_b), deepcopy(initial_c)
        pointer = 0
        output = []

        def read_combo_operand(p):
            p = program[p]
            if p in range(0, 4):
                return p
            else:
                registers = {4: a, 5: b, 6: c}
                return registers[p]

        while True:
            if pointer+1 >= len(program):
                break
            operation = program[pointer]
            pointer += 1
            inc = True
            if operation == 0: # adv
                a = int(a/(2**read_combo_operand(pointer)))
            elif operation == 1: # bxl
                # bitwise XOR of b and literal operand
                b = b ^ program[pointer]
            elif operation == 2: # bst
                b = read_combo_operand(pointer) % 8
            elif operation == 3: # jnz
                inc = False
                if a != 0:
                    pointer = program[pointer]
            elif operation == 4: # bxc
                # bitwise XOR of b and c
                b = b ^ c
            elif operation == 5: # out
                output.append(read_combo_operand(pointer) % 8)
            elif operation == 6: # bdv
                b = int(a/(2**read_combo_operand(pointer)))
            elif operation == 7: # cdv
                c = int(a/(2**read_combo_operand(pointer)))
            if inc:
                pointer += 1
        return output
    print(test_a(38886106775028))
    exit()
    mya = 1
    print(test_a(117440))
    last_good = 0
    while True:
        if len(test_a(mya)) == len(program):
            while True:
                if len(test_a(mya)) == len(program):
                    mya -= 1
                else:
                    break
            mya += 1
            # increment and check difference from program
            happened = False
            while True:
                output = test_a(mya)
                # r = len(shared_prefix(output, program))
                # print(r, len(output), len(program))
                # if output == program:
                #     print(mya)
                r = len(shared_prefix(output, program))
                if r > 9:
                    print(mya-last_good, r)
                    last_good = mya
                    happened = True
                if output == program:
                    print(mya)
                    exit()
                if len(output) > len(program):
                    print('''ghghghghghg''')
                    exit()
                mya += 131072 if happened else 1#024#327680
            exit()
        mya *= 2
    return

def part2(sample):
    registers, program = sample.split('\n\n')
    program = ints(program)

    def check_mya(mya):
        a, b, c = deepcopy(mya), 0, 0
        output = []
        while a != 0:
            # b is not dependent on previous iterations
            # thus the "ticker" is just a getting divided by 8
            b = (a & 7) ^ 2
            b = (b ^ (a//(1 << b))) ^ 3
            a = a >> 3
            output.append(b%8)
            # if not b % 8 == x:
            #     good = False
            #     break
        return output
    mya = 1 # maximum that has length 16
    matching = -1

    while matching != -17:
        output = check_mya(mya)
        if output[matching:] == program[matching:]:
            print(mya, output)
            mya *= 8
            matching -= 1
            # 37221261688308
            #
        else:
            mya += 1
    print(check_mya(mya))
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
