from utils import Grid, grid_from_string, ints
import networkx as nx
import functools

def grid_to_graph(grid: Grid):
    graph = nx.Graph()
    graph.add_nodes_from(grid.all_coordinates())
    for i in grid.all_where(lambda a: a != "_"):
        for j in i.straight_neighbors():
            if grid[j] and grid[j] != '_':
                graph.add_edge(i, j)
    return graph

inp = sys.stdin.read()
total = 0
for sample in inp.split():
    numgrid = grid_from_string('789\n456\n123\n_0A')
    numgraph = grid_to_graph(numgrid)
    dirgrid = grid_from_string('_^A\n<v>')
    dirgraph = grid_to_graph(dirgrid)
    pathmap = {(-1, 0): '<', (1, 0): '>', (0, -1): '^', (0, 1): 'v'}
    @functools.lru_cache
    def f(p1, p2, r):
        if r == 1:
            return nx.shortest_path_length(dirgraph, p1, p2) + 1
        graph = numgraph if r == 26 else dirgraph
        paths = nx.all_shortest_paths(graph, p1, p2)
        paths = [''.join([pathmap[path[i]-path[i-1]] for i in range(1, len(path))])+'A' for path in paths]

        min_cost = None
        for path in paths:
            cost = 0
            pos = dirgrid.index('A')
            for target in path:
                target = dirgrid.index(target)
                cost += f(pos, target, r-1)
                pos = target
            if min_cost == None or cost < min_cost:
                min_cost = cost
        return min_cost

    pos = numgrid.index('A')
    s = 0
    for target in sample:
        target = numgrid.index(target)
        s += f(pos, target, 26)
        pos = target
    total += s*ints(sample)[0]
print(total)
