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
FILE_PATH = f'{args.year}/d{args.day}/'

if not os.path.exists(FILE_PATH):
    os.makedirs(FILE_PATH)
    os.system('touch '+FILE_PATH+'main.py && cp template.py '+FILE_PATH+'main.py')

open(FILE_PATH+'input.txt', 'w').write(INPUT)

old_code = open(FILE_PATH+'main.py').read()
code = old_code

while True:
    old_code = code
    os.system('clear')
    print('#'*50)
    try:
        sys.stdin = StringIO(INPUT)
        exec(code)
    except Exception as e:
        #print(e)
        traceback.print_exc()
    n = 0
    while code == old_code and n < 30:
        code = open(FILE_PATH+'main.py').read()
        time.sleep(0.1)
        n += 1
"""Run the following before you commit to avoid any copyright issues (removing puzzle input):
find . -name "*.txt" -type f -delete
"""
# Cheers!
