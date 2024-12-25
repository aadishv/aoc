import typing
import re
import sys
from collections import Counter
from functools import reduce
from collections.abc import Iterator
from copy import deepcopy

sys.setrecursionlimit(10000)

# MARK: - vector class
class V(tuple):
    def __new__(cls, x: typing.Union[int, tuple], y: typing.Optional[int] = None) -> 'V':  # Create new vector
        if isinstance(x, tuple):
            return super().__new__(cls, x)
        return super().__new__(cls, (x, y))

    @property
    def x(self) -> int:  # X coordinate
        return self[0]

    @property
    def y(self) -> int:  # Y coordinate
        return self[1]

    def __add__(self, other: tuple) -> 'V':  # Add vectors
        return V(self.x + other[0], self.y + other[1])

    def __sub__(self, other: tuple) -> 'V':  # Subtract vectors
        return V(self.x - other[0], self.y - other[1])

    def __mul__(self, scalar: int) -> 'V':  # Multiply by scalar
        return V(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: int) -> 'V':  # Right multiply by scalar
        return self.__mul__(scalar)

    # MARK: - extra shtuff

    CARDINAL_DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    DIAGONAL_DIRECTIONS = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

    def window(self, width: int, height: int) -> list:  # Get window of coordinates
        return [[(i, j) for i in range(self.x, self.x+width)] for j in range(self.y, self.y+height)]

    def straight_neighbors(self) -> list:  # Get cardinal neighbors
        return [self+c for c in self.CARDINAL_DIRECTIONS]
    def diagonal_neighbors(self) -> list:  # Get diagonal neighbors
        return [self+c for c in self.DIAGONAL_DIRECTIONS]
    def neighbors(self, coord: tuple, restrict: bool = True) -> list:  # Get all neighbors
        return self.straight_neighbors(coord, restrict) + self.diagonal_neighbors(coord, restrict)
# MARK: - grid class
class Grid(dict[V, typing.Any]):
    def __missing__(self, key: tuple) -> None:  # Return None for missing keys
        return None

    @property
    def width(self) -> int:  # Width of grid
        return max([i[0] for i in self.keys()])+1
    @property
    def height(self) -> int:  # Height of grid
        return max([i[1] for i in self.keys()])+1

    def __init__(self, grid):
        self.update(grid)
        self.text = self.__str__

    def mass_at(self, list: list) -> list:  # Get values at coordinates
        return [self[i] for i in list]
    def mass_filter(self, list: list) -> list:  # Filter coordinates with values
        return [i for i in list if self[i]]
    def all_coordinates(self) -> list:  # Get all coordinates
        return list(self.keys())

    def column(self, n: int) -> list:  # Get column n
        return [self[(n, i)] for i in range(self.height)]
    def row(self, n: int) -> list:  # Get row n
        return [self[(i, n)] for i in range(self.width)]

    def convolution(self, width: int, height: int) -> list:  # Get overlapping windows
        returnv = []
        for y in range(self.height-height+1):
            row_convo = []
            for x in range(self.width-width+1):
                row_convo.append(self.window(x, y, width, height))
            returnv.append(row_convo)
        return returnv

    def all_where(self, fn) -> list:  # Get coordinates matching condition
        return [i for i in self.keys() if fn(self[i])]
    def index(self, v) -> tuple:  # Get first coordinate with value
        return self.all_where(lambda i: i == v)[0]
    def count(self, v) -> int:  # Count occurrences of value
        return sum([i == v for i in self.values()])

    def __str__(self) -> str:  # Get string representation
        text = ''
        for y in range(self.height):
            for x in range(self.width):
                text += str(self[(x, y)])
            text += '\n'
        return text

def grid_from_string(string: str, mapfn = lambda a: a) -> 'Grid':
    g = [[mapfn(j) for j in list(i)] for i in string.strip().split('\n') if i != '']
    grid = {}
    for i in range(len(g)):
        for j in range(len(g[i])):
            grid[V(j, i)] = g[i][j]
    return Grid(grid)


def grid_from_dimensions(width: int, height: int, default=None):  # Create empty grid with dimensions
    grid = {}
    for i in range(width):
        for j in range(height):
            grid[V(i, j)] = default
    return Grid(grid)
# MARK: - list functions
def list_split(list: list, length: int) -> list:  # Split list into fixed lengths
    result = []
    for _ in range(int(len(list)/length)):
        l = []
        for _ in range(length):
            l.append(list.pop(0))
        result.append(l)
    return result
def product(list: list) -> float:  # Multiply all elements
    return reduce(lambda a, b: a*b, list, 1)
def list_diff(x: list) -> list:  # Get differences between elements
    return [b-a for a, b in zip(x, x[1:])]
def list_range(x: int) -> list:  # Get range as list
    return list(range(x))
def lmap(func, *iterables) -> list:  # Map returning list
    return list(map(func, *iterables))
def unique(l: list) -> list:  # Get unique elements
    if type(l[0]) == list:
        return [list(i) for i in set(tuple(i) for i in l)]
    return list(set(l))
def flatten(l: list) -> list:  # Flatten nested lists
    return [item for sublist in l for item in sublist]
def remove_empty(l: list) -> list:  # Remove empty lists
    return [i for i in l if i != []]
def shared_elements(l1: list, l2: list) -> list:  # Get common elements
    return list(set(l1).intersection(set(l2)))
def distance_elements_loop(e1, e2, l):
    standard_distance = abs(l.index(e1) - l.index(e2))
    return min(standard_distance, len(l) - standard_distance)
def shared_prefix(*lists):
    """Find the shared prefix of a list of lists."""
    if not lists:
        return []

    # Find the shortest list
    shortest_list = min(lists, key=len)

    for i, element in enumerate(shortest_list):
        if not all(lst[i] == element for lst in lists):
            return shortest_list[:i]

    return shortest_list
# MARK: - misc
def ints(s: str) -> typing.List[int]:  # Extract integers from string
    return lmap(int, re.findall(r"-?\d+", s))  # thanks mserrano!
def regular_process(inp: str) -> list:  # Split and clean input
    return [i for i in inp.strip().split('\n') if i.strip != '']

def factorial(n: int) -> int:  # Calculate factorial
    if n==1:
        return 1
    return n*factorial(n-1)
def bit_not(n: int, numbits: int = 16) -> int:  # Bitwise not
        return (1 << numbits) - 1 - n

def partitions(n: int, k: int) -> list:  # Get integer partitions
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
def list_subtract(l1: list, l2: list) -> Iterator:  # Subtract list elements
    a = Counter(l1)
    b = Counter(l2)
    c = a - b  # ignores items in b missing in a
    return c.elements()
def length_consecutive(list: list) -> list:  # Get run lengths
    l = deepcopy(list)
    result = [0]
    c = l[0]
    while l:
        v = l.pop(0)
        if v == c:
            result[-1] += 1
        else:
            c = v
            result.append(1)
    return result
def runs(list: list, f) -> list:  # Split into runs by condition
    l = deepcopy(list)
    result = []
    currun = []
    while l:
        v = l.pop(0)
        nr = currun + [v]
        if f(nr):
            currun.append(v)
        else:
            result.append(currun)
            currun = [v]
    if currun != []:
        result.append(currun)
    return result
# MARK: - string utilities
def remove_char(string: str, v: str = ' ') -> str:  # Remove character from string
    string = ''.join([i for i in string if i != v])
    return string
def split_mult(string: str, charset: str) -> str:
    return [i for i in re.split("[" + re.escape(charset) + "]", string) if i != '']
# MARK: - dict utilities
def dict_invert(d: dict) -> dict:  # Invert dictionary
    return {v: k for k, v in d.items()}
