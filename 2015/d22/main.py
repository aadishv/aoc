import time
import random
import functools
from functools import reduce
import itertools
import math
import hashlib
import json
import re
import typing
from utils import *
import traceback
from copy import deepcopy
import collections
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



def solve(sample) -> int: # hp 51, damage 9
    output = 0
    # your mana, your hit point
    # boss hit points, boss damage
    # mana spent
    queue = [
        [(500, 50), (51, 9), 0]
    ]
    final = []
    while queue != []:
        print(len(queue))
        newqueue = []
        for game in queue:
            player, boss, cost = game
            options = {
                # change to thing, damage done, repeats
                'magic missile': (-53, 0, 0, 4, 1),
                'drain': (-73, 0, 2, 2, 1),
                'shield': (-113, 0, 0, 0, 6),
                'poison': (-173, 0, 0, 0, 6),
                'recharge': (-229, 101, 0, 0, 5)
            }
            for spell in options.keys():
                effect = options[spell]
                newplayer = deepcopy(player)
                newplayer = (newplayer[0] + effect[0], newplayer[1])
                add = True
                if newplayer[0] < 0: # make sure I'm not broke!
                    add = False
                effective_armor = 7 if spell == 'shield' else 0
                for _ in range(effect[-1]):
                    # player's turn
                    newplayer = (newplayer[0]+effect[1], newplayer[1]+effect[2])
                    boss = (boss[0] - effect[-2], boss[1])
                    if boss[0] <= 0:
                        final.append((newplayer, cost-effect[0]))
                        add = False
                    # boss's turn
                    newplayer = (newplayer[0] - max(1, boss[1] - effective_armor), newplayer[1])
                    if newplayer[1] <= 0:
                        add = False
                if add:
                    newqueue.append([player, boss, cost-effect[0]])
        queue = newqueue
    final = sorted(final, key=lambda x: x[1])
    print(final[0], final[-1])
    lines = regular_process(sample)

    return output


SAMPLE = """
"""
flag = 's'
if flag == 's':
    print(solve(SAMPLE))
if flag == 'i':
    print(solve(tester.INPUT))
