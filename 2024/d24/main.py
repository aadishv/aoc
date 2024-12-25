import sys
from copy import deepcopy
from utils import *
import re
inp = open('2024/d24/input.txt').read()#sys.stdin.read()
sample = """x00: 0
x01: 1
x02: 0
x03: 1
x04: 0
x05: 1
y00: 0
y01: 0
y02: 1
y03: 1
y04: 0
y05: 1

x00 AND y00 -> z05
x01 AND y01 -> z02
x02 AND y02 -> z01
x03 AND y03 -> z03
x04 AND y04 -> z04
x05 AND y05 -> z00
"""
# 114, 288, 241
values, paths = inp.strip().split('\n\n')

values = re.findall(r'(\w+): (1|0)', values)
values = {k: int(v) for k, v in values}

paths = re.findall(r'(\w+) (AND|XOR|OR) (\w+) -> (\w+)', paths)

vals_to_consider = [i for _, _, _, i in paths if i.startswith('z')]

paths = {j: (m, k, i) for i, k, m, j in paths}
rpaths = dict_invert(paths)

vals_to_consider = sorted(vals_to_consider, key=lambda i: ints(i)[0])
def get_val(a, op, b, log = False):
    v = rpaths.get((a, op, b), rpaths.get((b, op, a), None))
    if log:
        print(a, op, b)
    if not v and a and b:
        print(a, op, b, '                           not found')
    return v

print('z00', paths['z00'])
carry = get_val('x00', 'AND', 'y00')
print('Carry after z00:', carry)
for i in range(1, 45):
    print()
    intermediate_v = get_val('x{:02d}'.format(i), 'XOR', 'y{:02d}'.format(i))
    print("z{:02d} intermediate v".format(i), intermediate_v)
    v = get_val(intermediate_v, 'XOR', carry)
    print("z{:02d} v".format(i), get_val(intermediate_v, 'XOR', carry))
    intermediate_carry = get_val('x{:02d}'.format(i), 'AND', 'y{:02d}'.format(i))
    print("z{:02d} intermediate carry".format(i), intermediate_carry)
    intermediate_carry_2 = get_val(intermediate_v, 'AND', carry)
    print("z{:02d} intermediate carry 2".format(i), intermediate_carry_2)
    carry = get_val(intermediate_carry, 'OR', intermediate_carry_2)
    print("z{:02d} carry".format(i), carry)

print('\n\n\n')
print(','.join(sorted(["nbc", "svm", "kqk", "z15", "cgq", "z23", "fnr", "z39"])))
