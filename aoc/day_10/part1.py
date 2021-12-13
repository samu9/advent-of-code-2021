from utils import read_input

input_ = read_input(__file__)

closer = {
    "(": ")",
    "[": "]",
    "<": ">",
    "{": "}",
}

points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


def navigate(index, line):
    global points_sum
    char = line[index]

    next = index + 1
    while line[next] in closer.keys():
        # print(next)
        next = navigate(next, line)
        if not next:
            return False

    if line[next] != closer[char]:
        print(line[next])
        if line[next] not in closer.values():
            points_sum += points[line[next]]
        return False
    return next + 1


points_sum = 0
for i, line in enumerate(input_):
    for index, c in enumerate(line):
        navigate(index, line)
print(points_sum)
