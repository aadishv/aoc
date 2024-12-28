
# modified from `../d5/main.py`
import sys
from copy import deepcopy
from utils import *
import itertools
inp = sys.stdin.read()
sample = """3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10"""
ss = ints(sample)

def intcode_step(program, input, output, p):
    opcode = int(str(program[p])[-2:])
    def param(n):
        modes = list(reversed(str(program[p])[:-2]))
        parammode = 0
        if n-1 < len(modes):
            parammode = int(modes[n-1])
        if parammode == 0:
            return program[program[p+n]]
        elif parammode == 1:
            return program[p+n]

    new_program = program.copy()
    new_input = input.copy()
    new_output = output.copy()

    if opcode == 1:
        new_program[program[p+3]] = param(1)+param(2)
        return (new_program, new_input, new_output, p + 4, False)
    elif opcode == 2:
        new_program[program[p+3]] = param(1)*param(2)
        return (new_program, new_input, new_output, p + 4, False)
    elif opcode == 3:
        if not new_input:  # If input is empty
            return (new_program, new_input, new_output, p, False)
        v = new_input.pop(0)
        new_program[program[p+1]] = v
        return (new_program, new_input, new_output, p + 2, False)
    elif opcode == 4:
        new_output.append(param(1))
        return (new_program, new_input, new_output, p + 2, False)
    elif opcode == 5:
        if param(1) != 0:
            return (new_program, new_input, new_output, param(2), False)
        return (new_program, new_input, new_output, p + 3, False)
    elif opcode == 6:
        if param(1) == 0:
            return (new_program, new_input, new_output, param(2), False)
        return (new_program, new_input, new_output, p + 3, False)
    elif opcode == 7:
        if param(1) < param(2):
            new_program[program[p+3]] = 1
        else:
            new_program[program[p+3]] = 0
        return (new_program, new_input, new_output, p + 4, False)
    elif opcode == 8:
        if param(1) == param(2):
            new_program[program[p+3]] = 1
        else:
            new_program[program[p+3]] = 0
        return (new_program, new_input, new_output, p + 4, False)
    elif opcode == 99:
        return (new_program, new_input, new_output, p, True)
    return (new_program, new_input, new_output, p, False)

def intcode(program, input):
    p = 0
    curr_program = deepcopy(program)
    curr_input = input.copy()
    curr_output = []

    while p < len(curr_program):
        curr_program, curr_input, curr_output, p, done = intcode_step(curr_program, curr_input, curr_output, p)
        if done:
            break
    return curr_output, curr_program

best = -1
# for seq in itertools.permutations(range(5)):
#     c = 0
#     for i in range(5):
#         output, _ = intcode(ss, [seq[i], c])
#         c = output[0]
#     best = max(best, c)

best = -1
for seq in itertools.permutations(range(5, 10)):
    # Initialize amplifiers
    c1 = (deepcopy(ss), [seq[0], 0], [], 0, False)  # prog, input, output, pointer, halted
    c2 = (deepcopy(ss), [seq[1]], [], 0, False)
    c3 = (deepcopy(ss), [seq[2]], [], 0, False)
    c4 = (deepcopy(ss), [seq[3]], [], 0, False)
    c5 = (deepcopy(ss), [seq[4]], [], 0, False)

    while not all([c1[4], c2[4], c3[4], c4[4], c5[4]]):  # Continue until ALL amps halt
        # Run amp A
        c1 = intcode_step(*c1[:4])
        if c1[2]:  # If there's output
            c2[1].append(c1[2][-1])  # Add to input of next amp

        # Run amp B
        c2 = intcode_step(*c2[:4])
        if c2[2]:
            c3[1].append(c2[2][-1])

        # Run amp C
        c3 = intcode_step(*c3[:4])
        if c3[2]:
            c4[1].append(c3[2][-1])

        # Run amp D
        c4 = intcode_step(*c4[:4])
        if c4[2]:
            c5[1].append(c4[2][-1])

        # Run amp E
        c5 = intcode_step(*c5[:4])
        if c5[2]:
            c1[1].append(c5[2][-1])  # Feed back to amp A

    if c5[2]:  # If amp E produced any output
        final_output = c5[2][-1]
        best = max(best, final_output)


print(best)
