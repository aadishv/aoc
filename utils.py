import typing
import re
import sys
from collections import Counter
from functools import reduce
from collections.abc import Iterator

sys.setrecursionlimit(10000)
# MARK: - grid class
class Grid:
    CARDINAL_DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    DIAGONAL_DIRECTIONS = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
    def __init__(self, string, delimiter, mapfn=lambda a: a, pad=False):
        def delmsplit(s):
            if delimiter == '':
                return list(s)
            return s.split(delimiter)
        self.grid = [[mapfn(j) for j in delmsplit(i)] for i in [i for i in string.split('\n') if i != '']]
        max_length = max([len(i) for i in self.grid])
        if pad:
            for i in range(len(self.grid)):
                self.grid[i] += [None]*(max_length-len(self.grid[i]))
        self.width = max_length
        self.height = len(self.grid)
    def window(self, x, y, width, height):
        return [[self.grid[j][i] for i in range(x, x+width)] for j in range(y, y+height)]
    def column(self, n):
        return [row[n] for row in self.grid]
    def row(self, n):
        return self.grid[n]
    def in_bounds(self, coord):
        x, y = coord
        return 0 <= x < self.width and 0 <= y < self.height
    def convolution(self, width, height):
        returnv = []
        for y in range(len(self.grid)-height+1):
            row_convo = []
            for x in range(len(self.grid[0])-width+1):
                row_convo.append(self.window(x, y, width, height))
            returnv.append(row_convo)
        return returnv
    def straight_neighbors(self, coord):
        return [Grid.vector_add(coord, c) for c in CARDINAL_DIRECTIONS]
    def diagonal_neighbors(self, coord):
        return [Grid.vector_add(coord, c) for c in DIAGONAL_DIRECTIONS]
    def neighbors(self, coord):
        return [Grid.vector_add(coord, c) for c in CARDINAL_DIRECTIONS+DIAGONAL_DIRECTIONS]
    def all_coordinates(self):
        return reduce(lambda a,b: a+b, [[(i, j) for i in range(self.width)] for j in range(self.height)], [])
    def at(self, coord):
        x, y = coord
        return self.grid[y][x]
    def set(self, coord, v):
        x, y = coord
        self.grid[y][x] = v
    def first(self, cond):
        for y in range(self.height):
            for x in range(self.width):
                if cond(self.grid[y][x]):
                    return (x, y)
    def all_where(self, cond):
        o = []
        for y in range(self.height):
            for x in range(self.width):
                if cond(self.grid[y][x]):
                    o.append((x, y))
        return o
    def count(self, v):
        return sum([l.count(v) for l in self.grid])
    @staticmethod
    def vector_add(*vectors):
        return tuple([sum(i) for i in zip(*vectors)])
    @staticmethod
    def vector_multiply(vector, factor):
        return tuple([i*factor for i in vector])
    @staticmethod
    def vector_subtract(vector1, vector2):
        return Grid.vector_add(vector1, Grid.vector_multiply(vector2, -1))
# MARK: - list functions
def list_diff(x):
    return [b-a for a, b in zip(x, x[1:])]
def list_range(x):
    return list(range(x))
def lmap(func, *iterables):
    return list(map(func, *iterables))
def unique(l):
    return list(set(l))
def flatten(l):
    return [item for sublist in l for item in sublist]
# MARK: - misc
def ints(s: str) -> typing.List[int]:
    return lmap(int, re.findall(r"-?\d+", s))  # thanks mserrano!
def regular_process(inp):
    return [i for i in inp.strip().split('\n') if i.strip != '']

def factorial(n) -> int:
    if n==1:
        return 1
    return n*factorial(n-1)
def bit_not(n, numbits=16):
        return (1 << numbits) - 1 - n

def partitions(n, k):
    if k == 1:
        return [[n]]
    if k == n:
        return [[1] * n]
    if k > n:
        return []

    result = []
    for i in range(1, n - k + 2):
        for sub_partition in partitions(n - i, k - 1):
            result.append([i] + sub_partition)

    return result
def list_subtract(l1, l2):
    a = Counter(l1)
    b = Counter(l2)
    c = a - b  # ignores items in b missing in a
    return c.elements()
