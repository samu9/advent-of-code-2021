from utils import read_input, clamp


input_ = read_input(__file__)

levels = list(map(lambda i: list(map(int, i)), input_))

height = len(levels)
width = len(levels[0])
range_ = (0, height - 1)

steps = 100
flashes = 0


def get_neighbors(row, col):
    result = []
    for i in range(clamp(row - 1, range_), clamp(row + 1, range_) + 1):
        for j in range(clamp(col - 1, range_), clamp(col + 1, range_) + 1):
            if i == row and j == col:
                continue
            result.append([i, j])
    return result


def flash(row, col):
    global flashes
    flashes += 1
    flashed.append([row, col])
    neighbors = get_neighbors(row, col)
    for n in neighbors:
        if [n[0], n[1]] not in flashed:
            levels[n[0]][n[1]] += 1
            if levels[n[0]][n[1]] > 9:
                flash(n[0], n[1])
    levels[row][col] = 0


for s in range(steps):
    flashed = []
    levels = list(map(lambda l: list(map(lambda x: x + 1, l)), levels))
    for row, l in enumerate(levels):
        for col, _ in enumerate(l):
            if levels[row][col] > 9 and [row, col] not in flashed:
                flash(row, col)

print(flashes)


levels = list(map(lambda i: list(map(int, i)), input_))

step = 0
flashed = []
while len(flashed) < height * width:
    step += 1
    flashed = []
    levels = list(map(lambda l: list(map(lambda x: x + 1, l)), levels))
    for row, l in enumerate(levels):
        for col, _ in enumerate(l):
            if levels[row][col] > 9 and [row, col] not in flashed:
                flash(row, col)
print(step)
