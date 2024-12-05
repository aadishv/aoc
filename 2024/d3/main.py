SAMPLE_ANS = 48
DATE = (2024, 3)
# MARK: - end constants for testing
import re
# MARK: - helper fns from previous problems
def int_grid_from_string(s):
    grid = []
    for line in s.splitlines():
        if line != '':
            grid.append([int(j) for j in line.split(' ') if j != ''])
    max_length = max([len(i) for i in grid])
    for i in range(len(grid)):
        grid[i] += [None] * (max_length - len(grid[i]))
    return grid
def get_column_from_grid(grid, row):
    return [grid[i][row] for i in range(len(grid))]
def get_row_from_grid(grid, row):
    return grid[row]

def list_diff(x):
    return [b-a for a, b in zip(x, x[1:])]
def list_range(x):
    return list(range(x))

def lmap(func, *iterables):
    return list(map(func, *iterables))
def ints(s: str) -> typing.List[int]:
    return lmap(int, re.findall(r"-?\d+", s))  # thanks mserrano!

def parse_inp(inp):
    pos = [(0,0)]
    for j in inp:
        if j == '>':
            pos.append((pos[-1][0]+1, pos[-1][1]))
        elif j == '<':
            pos.append((pos[-1][0]-1, pos[-1][1]))
        elif j == '^':
            pos.append((pos[-1][0], pos[-1][1]+1))
        elif j == 'v':
            pos.append((pos[-1][0], pos[-1][1]-1))
    return pos
# MARK: - main function
def solve(inp):#
    output = 0
    good = True
    while inp:
        print(str(inp))
        if inp[:4] == "do()":
            inp = inp[4:]
            good = True
        elif inp[:7] == "don't()":
            inp = inp[7:]
            good = False
        elif inp[:4] == "mul(":
            inp = inp[4:]
            try:
                params = list(map(int, inp.split(')')[0].split(',')))
                if len(params) == 2 and good:
                    output += params[0] * params[1]
            except:
                pass
        else:
            inp = inp[1:]
    return output
