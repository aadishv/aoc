import sys
from copy import deepcopy
from utils import *
from test.test_re import B

inp = sys.stdin.read()
sample = """R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83"""
a = V(0,0)
b = V(0,0)

ap, bp = inp.strip().split('\n')
mm = {
    'U': V(0, 1),
    'D': V(0, -1),
    'L': V(-1, 0),
    'R': V(1, 0)
}
ap = ap.split(',')
bp = bp.split(',')
apath = []
print('dd')
for am in ap:
    apath += [  mm[am[0]]  ]*int(am[1:])
bpath = []
for am in bp:
    bpath += [  mm[am[0]]  ]*int(am[1:])

n = -1
print('repeats done')
ah = {}
s = 0
for am in apath:
    s += 1
    a = a + am
    if a not in ah:
        ah[a] = s
print('a done')
bh = {}
s = 0
for bm in bpath:
    s += 1
    b = b + bm
    if b not in bh:
        bh[b] = s
print('donee')
nn = 0
t = len(set(ah.values()) & set(bh.values()))
for p in set(ah) & set(bh):
    print(nn, t)
    nn += 1
    acost = ah[p]
    bcost = bh[p]
    cost = acost+bcost
    if cost < n or n == -1:
        n = cost#abs(p[0])+abs(p[1])
print(n)
exit()
