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
def check_if_loop(grid, starting):
    current = (starting, grid.CARDINAL_DIRECTIONS[0])
    visited = [(current[0], current[1])]  # Track position+direction pairs

    while True:
        try:
            next_pos = Grid.vector_add(*current)

            # Check if we're out of bounds
            if not (0 <= next_pos[0] < grid.width and 0 <= next_pos[1] < grid.height):
                return False

            if grid.at(*next_pos) == '#':
                # Turn right
                new_index = (grid.CARDINAL_DIRECTIONS.index(current[1]) + 1) % 4
                current = (current[0], grid.CARDINAL_DIRECTIONS[new_index])
            else:
                # Move forward
                current = (next_pos, current[1])

            # Check if we've seen this position+direction before
            state = (current[0], current[1])
            if state in visited:
                return True
            visited.append(state)

        except IndexError:
            return False

def solve(sample):
    grid = Grid(sample, '')
    starting = grid.first(lambda a: a == "^")
    count = 0

    # Try placing an obstacle at each empty position
    for pos in grid.all_coordinates():
        if grid.at(*pos) == '.' and pos != starting:
            new_grid = deepcopy(grid)
            new_grid.set(*pos, '#')
            if check_if_loop(new_grid, starting):
                count += 1

    return count


SAMPLE = """....#.....
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
flag = 'i'
if flag == 's':
    print(solve(SAMPLE))
if flag == 'i':
    print(solve(tester.INPUT))







# with open("2024/d6/input.txt", "r") as f:
#     grid = [list(i.strip()) for i in f.readlines()]

# def out(x, y):
#     return not (0 <= x < len(grid) and 0 <= y < len(grid[0]))

# ans1 = 0
# ans2 = 0

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# do = 0
# sx, sy = 0, 0
# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         if grid[i][j] == '^':
#             sx, sy = i, j

# def countvis(x, y, d):
#     vis = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
#     vist = [[[False for _ in range(4)] for _ in range(len(grid[0]))] for _ in range(len(grid))]
#     loop = False
#     while not out(x, y):
#         vis[x][y] = True
#         if vist[x][y][d]:
#             loop = True
#             break
#         vist[x][y][d] = True
#         if out(x + dx[d], y + dy[d]) or grid[x + dx[d]][y + dy[d]] != '#':
#             x += dx[d]
#             y += dy[d]
#         else:
#             d = (d + 1) % 4
#     return [sum(i.count(True) for i in vis), loop]

# ans1 = countvis(sx, sy, do)[0]

# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         if grid[i][j] != '#':
#             grid[i][j] = '#'
#             if countvis(sx, sy, do)[1]:
#                 ans2 += 1
#             grid[i][j] = '.'

# print(ans1)
# print(ans2)
# time.sleep(1000)
