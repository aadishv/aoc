""" gemini-genned comments
# Grid

*   **`__init__(self, string, delimiter, mapfn, pad=False)`:** Initializes a 2D grid from a string, using a delimiter to split cells and applying a mapping function to each cell, with optional padding.
*   **`window(self, x, y, width, height)`:** Returns a subgrid (window) of the specified dimensions starting at the given coordinates.
*   **`column(self, n)`:** Returns the nth column of the grid.
*   **`row(self, n)`:** Returns the nth row of the grid.
*   **`convolution(self, width, height)`:** Returns a list of all possible subgrids (windows) of the specified dimensions within the grid.

# List Functions

*   **`list_diff(x)`:** Returns a list of the differences between consecutive elements in the input list.
*   **`list_range(x)`:** Returns a list of integers from 0 to x-1.
*   **`lmap(func, *iterables)`:** Applies the given function to each element of the iterable(s) and returns a list of the results.

# Miscellaneous

*   **`ints(s: str) -> typing.List[int]`:** Extracts all integers from a string and returns them as a list.
*   **`regular_process(inp)`:** Cleans up an input string by removing empty lines and leading/trailing whitespace, returning a list of non-empty lines.¸
*   **`factorial(n)`:** Pretty self-explanatory
*   **`bit_not(n, numbits=16)`:** Bitwise not for n-bit number
****

max/min(inp, key=...)
sorted(iterator, key=...) (can use functools.cmp_to_key())
reversed(iterator)
reduced(function, iterator, initial)
"""
from test.test_signal import ItimerTest


def get_deer_at(deer, seconds):
    s = 0
    miles = 0
    phase = 'rest'
    while s <= seconds:
        if phase == 'rest':
            phase = 'fly'
            ogs = deepcopy(s)
            s = min(s + int(deer[2]), seconds)
            miles += (s-ogs)*int(deer[1])
        elif phase == 'fly':
            phase = 'rest'
            s += int(deer[-1])
    return miles
class Deer():
    def __init__(self, name, speed, flyt, restt):
        self.name = name
        self.speed = int(speed)
        self.flyt = int(flyt)
        self.restt = int(restt)
        self.phase = 'fly'
        self.time_remaining = self.flyt+0
        self.miles = 0
        self.points = 0
    def next_second(self):

        if self.time_remaining == 0:
            self.phase = [i for i in ['fly', 'rest'] if i != self.phase][0]
            self.time_remaining = self.flyt if self.phase == 'fly' else self.restt
        if self.phase == 'fly':
            self.miles += self.speed
        self.time_remaining -= 1
def solve(sample) -> int:
    output = 0

    lines = regular_process(sample)
    deer = re.findall(r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.", sample)
    deer = [Deer(*d) for d in deer]
    # name, speed km/s, fly time, rest time, phase, time remaining, points, miles
    for time in range(1, 2504):
        # update deer
        for d in deer:
            d.next_second()
        best = deer.index(max(deer, key=lambda d: d.miles))
        deer[best].points += 1
    best = deer.index(max(deer, key=lambda d: d.miles))
    deer[best].points += 1
    print([d.points for d in deer])

    return max(deer, key=lambda d: d.points).points


SAMPLE = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
"""
print(solve(tester.INPUT))
