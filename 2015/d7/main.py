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
"""
def solve(sample) -> int:
    def bit_not(n, numbits=16):
        return (1 << numbits) - 1 - n
    output = 0
    wires = {}
    for l in regular_process(sample):
        l = l.split(' -> ')
        wires[l[1]] = l[0]
    n = 0
    def parse(line):
        global n
        n += 1
        if n % 100000 == 0:
            print(n)
        if type(line) == int:
            return line
        if line.isnumeric():
            return int(line)
        if line in list(wires.keys()):
            if isinstance([line], int):
                pass
            else:
                wires[line] = parse(wires[line])
            return int(wires[line])
        if 'AND' in line:
            s = [parse(i) for i in line.split(' AND ')]
            return s[0] & s[1]
        if 'OR' in line:
            s = [parse(i) for i in line.split(' OR ')]
            return s[0] | s[1]
        if 'LSHIFT' in line:
            s = [parse(i) for i in line.split(' LSHIFT ')]
            return s[0] << s[1]
        if 'RSHIFT' in line:
            s = [parse(i) for i in line.split(' RSHIFT ')]
            return s[0] >> s[1]
        if 'NOT' in line:
            s = parse(line[4:])
            return bit_not(s)
    pa = parse('a')
    for l in regular_process(sample):
        l = l.split(' -> ')
        wires[l[1]] = l[0]
    wires['b'] = pa
    return parse('a')


SAMPLE = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
"""



# """
print(solve(tester.INPUT))
