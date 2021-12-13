from utils import read_input

input_ = read_input(__file__)

coords = list(map(lambda c: list(map(int, c.split(','))), input_[:input_.index('')]))
folds = map(lambda f: f.replace("fold along ", "").split("="), input_[input_.index('') + 1:])


def fold(coord, pos, list_):
    index = 0 if coord == "x" else 1
    points = []
    result = []
    for c in list_:
        if c[index] > int(pos):
            points.append(c)
        else:
            result.append(c)
    for p in points:
        new_point = [*p]
        new_point[index] = new_point[index] - 2 * (new_point[index] - int(pos))
        if new_point not in result:
            result.append(new_point)
    return result


for f in folds:
    coords = fold(*f, coords)

width = max(map(lambda c: c[0], coords)) + 1
height = max(map(lambda c: c[1], coords)) + 1
screen = [[" " for _ in range(width)] for _ in range(height)]

for c in coords:
    screen[c[1]][c[0]] = "*"
for s in screen:
    print("".join(s))