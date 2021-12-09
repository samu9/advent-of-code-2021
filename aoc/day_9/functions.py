from typing import List


def clamp(value: int, range_: List[int]):
    return min(max(range_[0], value), range_[1])


def get_adjacents(row, col, matrix) -> List[int]:
    height = len(matrix)
    width = len(matrix[0])
    adj = []
    if clamp(row-1, [0, height-1]) != row:
        adj.append([clamp(row-1, [0, height-1]), col])
    if clamp(row+1, [0, height-1]) != row:
        adj.append([clamp(row+1, [0, height-1]), col])
    if clamp(col-1, [0, height-1]) != col:
        adj.append([row, clamp(col-1, [0, width-1])])
    if clamp(col+1, [0, height-1]) != col:
        adj.append([row, clamp(col+1, [0, width-1])])
    return adj