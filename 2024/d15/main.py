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
    map = Grid(sample.split('\n\n')[0])
    moves = list(sample.split('\n\n')[1].strip())
    moves = [i for i in moves if i in ['<', '>', '^', 'v']]
    guard = map.all_where(lambda a: a == '@')[0]
    for move in moves:
        map.set(guard, '.')
        direction = {'<': (-1, 0), '>': (1, 0), '^': (0, -1), 'v': (0, 1)}[move]
        new_guard = Grid.vector_add(guard, direction)
        if map.at(new_guard) == '#':
            continue
        elif map.at(new_guard) == 'O':
            to_be_pushed = []
            good = True
            while True:
                if map.at(new_guard) == '.':
                    break
                if map.at(new_guard) == '#':
                    good = False
                    break
                elif map.at(new_guard) == 'O':
                    to_be_pushed.append(new_guard)

                new_guard = Grid.vector_add(new_guard, direction)
            if not good:
                map.set(guard, '@') # undo the deletion of the guard
                continue
            # have a list of things to push
            values = [map.at(i) for i in to_be_pushed]
            for p in range(len(to_be_pushed)):
                map.set(map.vector_add(to_be_pushed[p], direction), values[p])
        map.set(map.vector_add(guard, direction), '@')
        guard = map.vector_add(guard, direction)
    print('\n'.join([''.join(i) for i in map.grid]))
    print('\n\n\n')
    # calculate sum of GPS's
    total = 0
    for c in map.all_where(lambda a: a == 'O'):
        total += c[1]*100+c[0]
    print(total)
    return
def part2(sample):
    map = sample.split('\n\n')[0]
    moves = list(sample.split('\n\n')[1].strip())
    moves = [i for i in moves if i in ['<', '>', '^', 'v']]

    # double up map
    m = ''
    for l in list(map.split('\n')):
        f = ''
        for c in l:
            if c == 'O':
                f += '[]'
            elif c == '@':
                f += '@.'
            else:
                f += c*2

        m += f+'\n'
    map = Grid(m)

    guard = map.all_where(lambda a: a == '@')[0]
    n = 0
    for move in moves:
        n += 1
        print('Move', move, ':')
        map.set(guard, '.')
        direction = {'<': (-1, 0), '>': (1, 0), '^': (0, -1), 'v': (0, 1)}[move]
        new_guard = Grid.vector_add(guard, direction)
        if map.at(new_guard) == '#':
            continue
        elif map.at(new_guard) in ['[', ']']:
            to_be_pushed = [new_guard]
            if map.at(new_guard) == '[':
                to_be_pushed.append(Grid.vector_add(new_guard, (1, 0)))
            elif map.at(new_guard) == ']':
                to_be_pushed.append(Grid.vector_add(new_guard, (-1, 0)))
            good = True
            last_tbp = []
            while True:
                last_tbp = deepcopy(to_be_pushed)
                for ii in range(len(to_be_pushed)):
                    new = to_be_pushed[ii]
                    if map.at(new) == '.': # done for this thread
                        continue
                    elif map.at(new) == '#':
                        good = False
                        break
                    elif map.at(new) in ['[', ']']: # good
                        to_be_pushed.append(new)
                        nn = Grid.vector_add(new, (1, 0)) if map.at(new) == '[' else Grid.vector_add(new, (-1, 0))
                        to_be_pushed.append(nn)
                if not good:
                    break

                for i in to_be_pushed:
                    ni = Grid.vector_add(i, direction)
                    if map.at(ni) == '.':
                        continue
                    elif map.at(ni) == '#':
                        good = False
                        break
                    else:
                        to_be_pushed.append(ni)
                if not good:
                    break

                to_be_pushed = unique(to_be_pushed)
                if sorted(last_tbp) == sorted(to_be_pushed):
                    break
            if not good:
                map.set(guard, '@') # undo the deletion of the guard
                continue
            to_be_pushed = unique(to_be_pushed)
            # have a list of things to push
            if n < 0:
                for c in to_be_pushed:
                    map.set(c, 'L')
            else:
                values = [map.at(i) for i in to_be_pushed]
                for p in range(len(to_be_pushed)):
                    map.set(to_be_pushed[p], '.')
                for p in range(len(to_be_pushed)):
                    map.set(map.vector_add(to_be_pushed[p], direction), values[p])
        map.set(map.vector_add(guard, direction), '@')
        guard = map.vector_add(guard, direction)

    print('\n'.join([''.join(i) for i in map.grid]))
    # calculate sum of GPS's
    total = 0
    for c in map.all_where(lambda a: a == '['):
        total += c[1]*100+c[0]
    print(total)
    return

part = 2
flag = 'i'
SAMPLE = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""
"""#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^
"""
"""########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
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
