from utils import read_input

input_ = read_input(__file__)

levels = list(map(lambda i: list(map(int, i)), input_))

height = len(levels)
width = len(levels[0])

print(levels)

pos = [0, 0]
risk = 0


def traverse(pos, risk):
    while pos != [height - 1, width - 1]:
        if pos[0] == height - 1:
            risk += traverse([pos[0], pos[1] + 1], risk)

        if pos[1] == width - 1:
            risk += levels[pos[0] + 1][pos[1]]
            pos[0] += 1
        
    return risk

while pos != [width - 1, height - 1]:
    print(pos)
    if pos[0] == height - 1:
        risk += levels[pos[0]][pos[1] + 1]
        pos[1] += 1
        continue

    if pos[1] == width - 1:
        risk += levels[pos[0] + 1][pos[1]]
        pos[0] += 1
        continue

    if levels[pos[0]][pos[1] + 1] < levels[pos[0] + 1][pos[1]]:
        risk += levels[pos[0]][pos[1] + 1]
        pos[1] += 1
        continue

    if levels[pos[0]][pos[1] + 1] >= levels[pos[0] + 1][pos[1]]:
        risk += levels[pos[0] + 1][pos[1]]
        pos[0] += 1
        continue

print(risk)