# many of these imports are unused but may(?) be used by a solution, which executes in the same context as this file
import os
import time
from aocd.models import Puzzle
import argparse
import traceback

# argument parser
parser = argparse.ArgumentParser(description='Run the AOC solution given a day and year')
parser.add_argument('year', type=int,
                    help='Year of the solution')
parser.add_argument('day', type=int,
                    help='day of the solution')

os.system('echo "53616c7465645f5faf06e1b7542e94ee3d0f2cea81f82161354159e29c6ee6419261a697924e9a4b11f63197b1c4742cdb59ab41e4bb348dc5d6915f8b1d0b5f" > ~/.config/aocd/token')

class Tester:
    def __init__(self, date, input_path):
        self.puzzle = Puzzle(year=date[0], day=date[1])
        self.INPUT = self.puzzle.input_data
        open(input_path+'input.txt', 'w').write(self.puzzle.input_data)

args = parser.parse_args()
DATE = (args.year, args.day)
FILE_PATH = f'{args.year}/d{args.day}/'

tester = Tester(DATE, FILE_PATH)
old_code = open(FILE_PATH+'main.py').read()
code = old_code

while True:
    old_code = code
    os.system('clear')
    print('#'*50)
    try:
        exec(code)
    except Exception as e:
        #print(e)
        traceback.print_exc()
    n = 0
    while code == old_code and n < 10:
        code = open(FILE_PATH+'main.py').read()
        time.sleep(0.1)
        n += 1
"""Run the following before you commit to avoid any copyright issues (removing puzzle input):
find . -name "*.txt" -type f -delete
"""
# Cheers!
