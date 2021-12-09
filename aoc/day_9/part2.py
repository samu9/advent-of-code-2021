from functools import reduce

from utils import read_input
from aoc.day_9.functions import get_adjacents


input_ = read_input(__file__)
matrix = [list(map(int, x)) for x in input_]
height = len(matrix)
width = len(matrix[0])


def explore_basin(row, col, size=0, visited=[]):
    visited.append([row, col])
    adj = get_adjacents(row, col, matrix)
    for a in adj:
        if a not in visited and 9 > matrix[a[0]][a[1]] > matrix[row][col]:
            size += 1 + explore_basin(a[0], a[1], 0, visited)
    return size


sizes = []


for row in range(height):
    for col in range(width):
        adj = get_adjacents(row, col, matrix)
        if all(map(lambda x: matrix[x[0]][x[1]] > matrix[row][col], adj)):
            sizes.append(explore_basin(row, col, 1))
sizes.sort(reverse=True)

print(reduce(lambda x, y: x * y, sizes[0:3]))
