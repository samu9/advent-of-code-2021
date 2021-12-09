from functions import get_adjacents


with open("aoc/day_9/input.txt") as fp:
    input_ = fp.read().splitlines()

matrix = [list(map(int, x)) for x in input_]
height = len(matrix)
width = len(matrix[0])


def explore_basin(row, col, size=0, coords=[]):
    adj = get_adjacents(row, col, matrix)
    for a in adj:
        if a not in coords and matrix[row][col] < matrix[a[0], a[1]] < 9:
            size += 1
            coords.append(a)
            return explore_basin(a[0], a[1], size=size, coords=coords)
    return size

sizes = []
for row in range(height):
    for col in range(width):
        adj = get_adjacents(row, col, matrix)
        if all(map(lambda x: x > matrix[row][col], adj)):
            sizes.append(explore_basin(row, col))

risk_sum = 0
