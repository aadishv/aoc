import sys
sys.path.append('../../')
from utils import *
from copy import deepcopy
"""########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""
sample = """##########
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
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""
inp = open('input.txt').read()

s = inp
s = s.split('\n\n')
grid = grid_from_string(s[0])
current_pos = grid.index('@')
movements = {'<': V(-1, 0), '>': V(1, 0), '^': V(0, -1), 'v': V(0, 1)}
for instr in s[1].strip():
    print(instr)
    if instr not in movements:
        continue
    good = True
    to_move = []
    next_pos = current_pos
    while True:
        if grid[next_pos] == '#':
            good = False
            break
        elif grid[next_pos] == '.':
            break
        to_move.append(next_pos)
        next_pos += movements[instr]
    if good:
        values = [grid[v] for v in to_move]
        for i in to_move:
            grid[i] = '.'
        for i,j in zip(to_move, values):
            grid[i+movements[instr]] = j
    current_pos = grid.index('@')
s = 0
for i in grid.all_where(lambda a: a == 'O'):
    s += i[0] + i[1]*100
s
