import typing
import re
import sys

sys.setrecursionlimit(10000)
# MARK: - grid class
class Grid:
    def __init__(self, string, delimiter, mapfn, pad=False):
        def delmsplit(s):
            if delimiter == '':
                return list(s)
            return s.split(delimiter)
        self.grid = [[mapfn(j) for j in delmsplit(i)] for i in string.split('\n')]
        if pad:
            max_length = max([len(i) for i in self.grid])
            for i in range(len(self.grid)):
                self.grid[i] += [None]*(max_length-len(self.grid[i]))
    def window(self, x, y, width, height):
        return [[self.grid[j][i] for i in range(x, x+width)] for j in range(y, y+height)]
    def column(self, n):
        return [row[n] for row in self.grid]
    def row(self, n):
        return self.grid[n]
    def convolution(self, width, height):
        returnv = []
        for y in range(len(self.grid)-height+1):
            row_convo = []
            for x in range(len(self.grid[0])-width+1):
                row_convo.append(self.window(x, y, width, height))
            returnv.append(row_convo)
        return returnv
# MARK: - list functions
def list_diff(x):
    return [b-a for a, b in zip(x, x[1:])]
def list_range(x):
    return list(range(x))
def lmap(func, *iterables):
    return list(map(func, *iterables))
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
