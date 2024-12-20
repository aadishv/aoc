from utils import *
import networkx as nx

def build_graph(grid: Grid, allow_walls: bool = False) -> nx.Graph:
    G = nx.Graph()
    for pos in grid.all_coordinates():
        if not allow_walls and grid[pos] == '#':
            continue
        for new in pos.straight_neighbors():
            if (new in grid) and (allow_walls or grid[new] in '.SE'):
                G.add_edge(pos, new, weight=1)
    return G

def part1(sample):
    grid = grid_from_string(sample.strip())
    G = build_graph(grid)
    first = nx.shortest_path_length(G, grid.index('S'), grid.index('E'))
    start = tuple(grid.index('S'))
    end = tuple(grid.index('E'))
    valid = [tuple(i) for i in grid.all_where(lambda a: a in '.SE')]

    @lru_cache
    def get_path(a, b):
        return nx.shortest_path_length(G, a, b)

    count = 0
    for p1, p2 in itertools.permutations(valid, 2):
        cc = abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
        if cc > 20:
            continue
        time1 = get_path(start, p1)
        if time1 > first:
            continue
        time3 = get_path(p2, end)
        total = time1 + cc + time3
        if first-total == 76:
            newg = deepcopy(grid)
            newg[p1], newg[p2] = '1', '2'
            print(newg)
            count += 1
    print('Count:', count)
    return

def part2(sample):
    grid = grid_from_string(sample.strip())
    G = build_graph(grid)
    G_walls = build_graph(grid, allow_walls=True)

    first = nx.shortest_path_length(G, grid.index('S'), grid.index('E'))
    start = tuple(grid.index('S'))
    end = tuple(grid.index('E'))

    start_distances = nx.single_source_dijkstra_path_length(G, start, weight='weight')
    end_distances = nx.single_source_dijkstra_path_length(G, end, weight='weight')

    count = 0
    total = len(grid.all_where(lambda a: a in '.SE'))

    for i, cheat_start in enumerate(grid.all_where(lambda a: a in '.SE')):
        print(f'Progress: {i}/{total}')
        cheat_ends = nx.single_source_dijkstra_path_length(G_walls, cheat_start, cutoff=20)
        initial_time = start_distances[cheat_start]

        for end_pos, steps in cheat_ends.items():
            if grid[end_pos] not in '.E':
                continue
            cheat_time = initial_time + steps + end_distances[end_pos]
            if first - cheat_time >= 100:
                count += 1

    print(f'Final count: {count}')
    return count

part = 2
flag = 'i'
SAMPLE = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
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
