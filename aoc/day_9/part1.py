from typing import List


with open("aoc/day_9/input.txt") as fp:
    input_ = fp.read().splitlines()

matrix = [list(map(int, x)) for x in input_]

height = len(matrix)
width = len(matrix[0])

risk_sum = 0
def clamp(value: int, range_: List[int]):
    return min(max(range_[0], value), range_[1])


def get_adjacents(row, col):
    adj = []
    if clamp(row-1, [0, height-1]) != row:
        adj.append(matrix[clamp(row-1, [0, height-1])][col])
    if clamp(row+1, [0, height-1]) != row:
        adj.append(matrix[clamp(row+1, [0, height-1])][col])
    if clamp(col-1, [0, height-1]) != col:
        adj.append(matrix[row][clamp(col-1, [0, width-1])])
    if clamp(col+1, [0, height-1]) != col:
        adj.append(matrix[row][clamp(col+1, [0, width-1])])
    return adj


for row in range(height):
    for col in range(width):
        adj = get_adjacents(row, col)
        if all(map(lambda x: x > matrix[row][col], adj)):
            risk_sum += matrix[row][col] + 1

print(risk_sum)