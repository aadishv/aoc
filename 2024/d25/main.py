import sys
from copy import deepcopy
from utils import *
import itertools
inp = sys.stdin.read()
sample = """#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####
"""
s = inp
s = [grid_from_string(i) for i in s.strip().split('\n\n')]
locks = [g for g in s if all([i == '#' for i in g.row(0)])]
keys = [g for g in s if all([i == '#' for i in g.row(g.height-1)])]
# for lock in locks:
#     print([lock.column(i).count('#')-1 for i in range(locks[0].width)])
# print('\n\n\n')
# for key in keys:
#     print([key.column(i).count('#')-1 for i in range(locks[0].width)])
height = keys[0].height
n = 0
for lock, key in itertools.product(locks, keys):
    lock = [lock.column(i).count('#')-1 for i in range(locks[0].width)]
    key = [key.column(i).count('#')-1 for i in range(locks[0].width)]
    newk = [i+j for i,j in zip(lock, key)]
    if max(newk) < height-1:
        n += 1
print(n)
