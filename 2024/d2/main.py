import sys
sys.path.append('../../')
from utils import *
from copy import deepcopy

sample = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""
inp = open('input.txt').read()

s = inp
reports = regular_process(s)
t = 0
for i in reports:
    report = ints(i)
    diff = list_diff(report)
    if len(unique([1 if i > 0 else -1 if i < 0 else 0 for i in diff])) == 1:
        #print(report)
        if diff[0] != 0 and all([abs(i) in [1,2,3] for i in diff]):
            t += 1
print(t)
def check_report(report):
    diff = list_diff(report)
    if len(unique([1 if i > 0 else -1 if i < 0 else 0 for i in diff])) == 1:
        #print(report)
        if diff[0] != 0 and all([abs(i) in [1,2,3] for i in diff]):
            return True
    return False
t = 0
for r in reports:
    report = ints(r)
    if check_report(report):
        t += 1
        continue
    else:
        for i in range(len(report)):
            newr = report[:i] + report[i+1:]
            if check_report(newr):
                t += 1
                break
print(t)
