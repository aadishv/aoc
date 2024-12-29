# many of these imports are unused but may(?) be used by a solution, which executes in the same context as this file
import os
import time
from aocd.models import Puzzle
import argparse
import traceback
import sys
from io import StringIO

# argument parser
parser = argparse.ArgumentParser(description='Run the AOC solution given a day and year')
parser.add_argument('year', type=int,
                    help='Year of the solution')
parser.add_argument('day', type=int,
                    help='day of the solution')

args = parser.parse_args()
INPUT = Puzzle(year=args.year, day=args.day).input_data
CODE_PATH = f'src/{args.year}/d{args.day}.rs'
INPUT_PATH = f'src/inputs/{args.year}/d{args.day}.txt'

if not os.path.exists(CODE_PATH):
    os.system(f'touch {CODE_PATH} && cp template.rs {CODE_PATH}')

if not os.path.exists(INPUT_PATH):
    os.system(f'touch {INPUT_PATH}')
open(INPUT_PATH, 'w').write(INPUT)

old_code = open(CODE_PATH).read()
code = old_code

while True:
    old_code = code
    os.system(f'clear && cargo run < {INPUT_PATH}')

    n = 0
    while code == old_code and n < 50:
        code = open(CODE_PATH).read()
        time.sleep(0.1)
        n += 1
