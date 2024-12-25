import sys
from copy import deepcopy
from utils import *
import itertools
from collections import defaultdict
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

network = defaultdict(set)
for a, b in pairs:
    network[a].add(b)
    network[b].add(a)
# all_comps is a list of all nodes
# network is a map from each node to a list of its neighbors
def icky(current_clique, candidates, excluded) -> int:
    print(len(current_clique))
    # given the current parameters, return the max possible clique (recursive)
    # parameters at beginning: [], all_comps, []
    # base case: candidates is empty, return len(current_clique)
    if len(candidates) == 0:
        return current_clique
    # loop through all candidates. for each candidate, create new set of inputs with new cands/excluded
    best = []
    pivot = min(candidates, key=lambda node: len(network[node]))
    for candidate in candidates - network[pivot]:
        # we are assuming candidate is viable
        new_clique = current_clique + [candidate]
        new_candidates = candidates & network[candidate]
        new_excluded = excluded & network[candidate]
        best_clique = icky(new_clique, new_candidates, new_excluded)
        if len(best_clique) > len(best):
            best = best_clique
    return best
print(','.join(sorted(icky([], set(all_comps), set()))), 'answer')
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
