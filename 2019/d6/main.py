import sys
from copy import deepcopy
from utils import *
from collections import defaultdict

inp = sys.stdin.read()
sample = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN
"""

s = lmap(lambda i: tuple(i.split(')')), regular_process(inp))
orbits = defaultdict(list)
for a, b in s:
    orbits[a].append(b)

queue = lmap(lambda i: [i], orbits.keys())
n = 0
while queue != []:
    # print(len(queue))
    newq = []
    for o in queue:
        for neighbor in orbits[o[-1]]:
            if neighbor in o:
                continue
            n += 1
            newq.append(o+[neighbor])
    queue = unique(newq)
print("part 1:", n)

s = lmap(lambda i: tuple(i.split(')')), regular_process(inp))
orbits = defaultdict(list)
for a, b in s:
    orbits[a].append(b)
    orbits[b].append(a)

you_orbiting = orbits['YOU'][0]
san_orbiting = orbits['SAN'][0]

queue = [[you_orbiting]]
while queue != []:
    # print(len(queue))
    newq = []
    for o in queue:
        if o[-1] == san_orbiting:
            print('part 2:', len(o)-1)
            exit()
        # print(o, orbits[o[-1]])
        neighbors = orbits[o[-1]]# + [k for k in orbits.keys() if o[-1] in orbits[k]]
        for neighbor in neighbors:
            if neighbor in o:
                continue
            newq.append(o+[neighbor])
    queue = newq
