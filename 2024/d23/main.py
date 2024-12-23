import sys
from copy import deepcopy
from utils import *
import itertools
import collections as colls
import networkx

inp = sys.stdin.read()
sample = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
"""

matches = []
pairs = [i.split('-') for i in inp.strip().split('\n')]

all_comps = flatten(map(list, pairs))

G = networkx.Graph()
G.add_nodes_from(all_comps)
for pair in pairs:
    G.add_edge(*pair)
    G.add_edge(*reversed(pair))

# queue = set(lmap(lambda i: tuple([i]), all_comps))
# final = set()
# while len(queue) > 0:
#     print(len(queue))
#     newq = set()
#     for network in queue:
#         for n in all_comps:
#             if all([n in options[i] for i in network]) and n not in network:
#                 newq.add(tuple(sorted(list(network) + [n])))
#         else:
#             final.add(tuple(sorted(network)))
#     queue = newq
print(','.join(sorted(max(networkx.find_cliques(G),key=len))))
#     #print(n, total)
#     n += 1

#     ops = options[first]
#     for second in ops:
#         for third in ops.intersection(options[second]):
#             if True:#any(['t' in a for a in [first, second, third]]):
#                 tris.add(
#                     tuple(
#                         sorted([first, second, third])
#                     )
#                 )
# tttt = sum(1 for triangle in tris
#                     if any(node.startswith('t') for node in triangle))
# print(tttt)
#print(len(unique(newm)))
