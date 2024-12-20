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
from functools import cmp_to_key
import math
import itertools

def part1(sample):
    def rank(a):
        # stronger = higher rank
        # figure out the other rank
        vals = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
        print(len(vals))
        orank = [vals.index(i) for i in a]

        cons = sorted(length_consecutive(sorted(a)))

        value = 0
        if cons == [5]: # five of a kind
            value = 1
        elif cons == [1, 4]: # four of a kind
            value = 2
        elif cons == [2, 3]: # full houes
            value = 2.5
        elif cons == [1, 1, 3]: # three of a kind
            value = 3
        elif cons == [1, 2, 2]: # two pairs
            value = 4
        elif cons == [1, 1, 1, 2]: # one pair
            value = 5
        elif cons == [1]*5: # high card
            value = 6
        return [value]+orank
    decks = [(i.split()[0], int(i.split()[1])) for i in sample.split('\n') if i != '']
    decks = list(reversed(sorted(decks, key=lambda i: rank(i[0]))))
    decks = sum([v[1]*(i+1) for i, v in enumerate(decks)])
    print(decks)
    # bitshift 4 each time
    return
def part2(sample):
    def rank_given_cons(cons):
        value = 0
        if cons == [5]: # five of a kind
            value = 1
        elif cons == [1, 4]: # four of a kind
            value = 2
        elif cons == [2, 3]: # full houes
            value = 2.5
        elif cons == [1, 1, 3]: # three of a kind
            value = 3
        elif cons == [1, 2, 2]: # two pairs
            value = 4
        elif cons == [1, 1, 1, 2]: # one pair
            value = 5
        elif cons == [1]*5: # high card
            value = 6
        return value
    def rank(a):
        # stronger = higher rank
        # figure out the other rank
        vals = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

        orank = [vals.index(i) for i in a]

        cons = sorted(a)
        js = cons.count('J')
        if js == 0:
            return [rank_given_cons(sorted(length_consecutive(cons)))]+orank
        cons = [i for i in cons if i != 'J']
        best_hand_rank = 6
        for i in itertools.product([i for i in vals if i != 'J'], repeat = js):
            mycons = sorted(cons+list(i))
            rank = rank_given_cons(sorted(length_consecutive(mycons)))
            if rank < best_hand_rank:
                best_hand_rank = rank

        value = 0
        print(a, best_hand_rank)
        return [best_hand_rank]+orank
    decks = [(i.split()[0], int(i.split()[1])) for i in sample.split('\n') if i != '']
    decks = list(reversed(sorted(decks, key=lambda i: rank(i[0]))))
    print(decks)
    decks = sum([v[1]*(i+1) for i, v in enumerate(decks)])
    print(decks)
    # bitshift 4 each time
    return

part = 2
flag = 'i'
SAMPLE = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
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
