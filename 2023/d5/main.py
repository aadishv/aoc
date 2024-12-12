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
from functools import lru_cache
from collections import defaultdict

class mydict(dict):
    def __missing__(self, key):
        return key

def part1(sample) -> int:
    inputs = sample.strip().split('\n\n')
    inputs = [remove_empty([ints(j) for j in regular_process(i)]) for i in inputs]
    def process_to_dict(dict):
        d = mydict()
        for i in dict:
            r = range(i[1], i[1]+i[2])
            for j in r:
                d[j] = i[0]+(j-i[1])
        return d
    seeds = inputs[0][0]
    seed_to_soil = process_to_dict(inputs[1])
    soil_to_fertilizer = process_to_dict(inputs[2])
    fertilizer_to_water = process_to_dict(inputs[3])
    water_to_light = process_to_dict(inputs[4])
    light_to_temperature = process_to_dict(inputs[5])
    temperature_to_humidity = process_to_dict(inputs[6])
    humidity_to_location = process_to_dict(inputs[7])

    def get_location(ns):
        ns = unique([seed_to_soil[n] for n in ns])
        ns = unique([soil_to_fertilizer[n] for n in ns])
        ns = unique([fertilizer_to_water[n] for n in ns])
        ns = unique([water_to_light[n] for n in ns])
        ns = unique([light_to_temperature[n] for n in ns])
        ns = unique([temperature_to_humidity[n] for n in ns])
        ns = unique([humidity_to_location[n] for n in ns])
        return ns
    r = set()
    while seeds != []:
        s = seeds.pop(0)
        for i in range(s, s+seeds.pop(0)):
            r.add(i)
    print(len(r))
    print(min(get_location(r)))
    return
def part2(sample):
    return

part = 1
flag = 'i'
SAMPLE = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
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
