exec(open('../../utils.py').read())
from copy import deepcopy

sample = """"""
inp = open('input.txt').read()

x = list_split(ints(inp), 2)
x = zip(sorted([i[0] for i in x]), sorted([i[1] for i in x]))
print(sum([abs(i-j) for i,j in x]))

x = list_split(ints(inp), 2)
x1 = [i[0] for i in x]
x2 = [i[1] for i in x]
print(sum([i*x2.count(i) for i in x1]))
