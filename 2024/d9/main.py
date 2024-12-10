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

def part1(sample) -> int:
    sample = list(sample.strip())
    state = []
    n = 0
    while sample != []:
        state += [n]*int(sample.pop(0))
        if sample != []:
            state += [-1]*int(sample.pop(0))
        n += 1

    for i in range(len(state)):
        if state[i] == -1:
            for j in reversed(range(i+1, len(state))):
                if state[j] != -1:
                    state[i], state[j] = state[j], state[i]
                    break
    print(sum([i*int(v) for i, v in enumerate(state) if v != -1]))
def part2(sample):
    print('sdgdfgdf')
    sample = list(sample.strip())
    state = []
    n = 0
    while sample != []:
        state.append((n, int(sample.pop(0))))
        if sample != []:
            state.append((-1, int(sample.pop(0))))
        n += 1
    print("SDSFGDGH")
    g = 0
    move = reversed([j for i,j in enumerate(state) if j[0] != -1])

    for block_to_move in move:
        g += 1
        print(g)
        index_of_block_to_move = state.index(block_to_move)
        block_replace = [(i, j) for i,j in enumerate(state) if j[0] == -1 and j[1] >= block_to_move[1] and i < index_of_block_to_move]
        if block_replace == []:
            continue
        index_of_block_replace, block_replace = block_replace[0]
        toadd = [block_to_move, (-1, block_replace[1]-block_to_move[1])]
        state = state[:index_of_block_replace] + toadd + state[index_of_block_replace+1:]
        state[index_of_block_to_move + len(toadd)-1] = (-1, block_to_move[1])

    c = 0
    j = [[str(j[0]) if j[0] != -1 else '.'] * j[1] for j in state]
    j = [item for sublist in j for item in sublist]
    print(''.join(j))
    print(sum([i*int(v) for i, v in enumerate(j) if v != '.']))
SAMPLE = """2333133121414131402"""
#00992111777.44.333....5555.6666.....8888..
#00992111777.44.333....5555.6666.....8888..
part = 2
flag = 'i'
solve = part1 if part == 1 else part2
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
