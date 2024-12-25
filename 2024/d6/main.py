import sys
from copy import deepcopy
from utils import *

inp = sys.stdin.read()
sample = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""
g = grid_from_string(inp.strip())
pos = g.index('^')
dir = V(0, -1) # up
n = 0
history = set()
while pos in g:
    history.add(pos)
    nextpos = pos + dir
    if nextpos not in g:
        break
    elif g[nextpos] == '#':
        dir = V.CARDINAL_DIRECTIONS[(V.CARDINAL_DIRECTIONS.index(dir) + 1) % 4]
    else:
        pos = nextpos
        n += 1

print('part 1:', len(history))


spos = g.index('^')
myh = set(history)
def check_loop(changed):
    pos = deepcopy(spos)
    dir = V(0, -1) # up
    history = set()
    while pos in g:
        nextpos = pos + dir
        if nextpos not in g:
            break
        elif g[nextpos] == '#' or nextpos == changed:
            if (pos, dir) in history:
                return True
            history.add((pos, dir))
            dir = V.CARDINAL_DIRECTIONS[(V.CARDINAL_DIRECTIONS.index(dir) + 1) % 4]
        else:
            pos = nextpos
    #print(grid)
    return False
n = 0
k = 0
for possible in myh:
    if possible == spos:
        continue
    print(k+1, len(myh))
    k += 1
    if check_loop(possible):
        n += 1
print('part 2:', n)
