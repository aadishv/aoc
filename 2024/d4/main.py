def solve(sample):#
    print(time.time())
    grid = Grid(sample, '', lambda x: x)
    convolutions = reduce(lambda x, y: x + y, grid.convolution(3, 3), [])

    output = 0
    for i in convolutions:
        if i[1][1] == 'A':
            x1 = [i[0][0], i[2][2]]
            x2 = [i[0][2], i[2][0]]
            if all([j in [['M', 'S'], ['S', 'M']] for j in [x1, x2]]):
                output += 1
    print(time.time())
    return output


SAMPLE = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
print(solve(tester.INPUT))
time.sleep(1)
