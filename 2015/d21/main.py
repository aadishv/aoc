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


from re import X


weapons = """
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0
"""
armor = """
Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5
"""
rings = """
Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
"""
weapons = [[int(i) for i in j] for j in re.findall(r'(\d+)\s+(\d+)\s+(\d+)', weapons)]
armor = [[int(i) for i in j] for j in re.findall(r'(\d+)\s+(\d+)\s+(\d+)', armor)] + [(0,0,0)]

rings = [[int(i) for i in j] for j in re.findall(r'(\d+)\s+(\d+)\s+(\d+)', rings)]
rings = reduce(lambda a,b: a+b, [[(r, i) for r in rings if r != i] for i in rings], [])

rings = [(int(a[0])+int(b[0]), int(a[1])+int(b[1]), int(a[2])+int(b[2])) for (a,b) in rings] + [(0,0,0)]

def solve(sample) -> int:
    output = 0
    for ring in rings:
        for a in armor:
            for weapon in weapons:
                print("!", end="")
    # We need to ensure that:
        # my hit points/(9 - my armor)<=103/(my damage - 2)=t
    lines = regular_process(sample)

    return output


SAMPLE = """
"""
flag = 's'
if flag == 's':
    print(solve(SAMPLE))
if flag == 'i':
    print(solve(tester.INPUT))
