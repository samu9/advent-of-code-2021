from utils import read_input
from aoc.day_9.functions import get_adjacents

input_ = read_input(__file__)

matrix = [list(map(int, x)) for x in input_]
height = len(matrix)
width = len(matrix[0])

risk_sum = 0


for row in range(height):
    for col in range(width):
        adj = get_adjacents(row, col, matrix)
        if all(map(lambda x: x > matrix[row][col], adj)):
            risk_sum += matrix[row][col] + 1

print(risk_sum)