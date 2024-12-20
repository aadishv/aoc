from utils import *
import os
import time
from aocd.models import Puzzle
import argparse
import traceback

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

args = parser.parse_args()
DATE = (args.year, args.day)
FILE_PATH = f'{args.year}/d{args.day}/'

if not os.path.exists(FILE_PATH):
    os.makedirs(FILE_PATH)
    os.system('touch '+FILE_PATH+'main.py && cp template.py '+FILE_PATH+'main.py')

tester = Tester(DATE, FILE_PATH)
if not os.path.exists(FILE_PATH+'input.txt'):
    open(FILE_PATH+'input.txt', 'w').write(tester.INPUT)
