from utils import read_input

input_ = read_input(__file__)

paths = []


def build_graph():
    graph = {}

    for i in input_:
        paths = i.split("-")
        if paths[0] != "end" and paths[1] != "start":
            if paths[0] not in graph:
                graph[paths[0]] = [paths[1]]
            else:
                graph[paths[0]].append(paths[1])
        if paths[1] != "end" and paths[0] != "start":
            if paths[1] not in graph:
                graph[paths[1]] = [paths[0]]
            else:
                graph[paths[1]].append(paths[0])
    return graph


def explore(cave="start", steps=["start"]):
    global graph
    for g in graph[cave]:
        if g.islower() and g in steps:
            continue
        if g == 'end':
            paths.append([*steps, g])
            continue
        explore(g, [*steps, g])


def explore2(cave="start", steps=["start"], small_count={}):
    global graph

    for g in graph[cave]:
        if g == 'end':
            paths.append([*steps, g])
            continue
        new_count = dict(small_count)
        if g.islower():
            if g not in new_count:
                new_count[g] = 0
            if new_count[g] >= 1 and any(map(lambda x: x > 1, new_count.values())):
                continue
            new_count[g] += 1
        explore2(g, [*steps, g], new_count)


graph = build_graph()
explore2()

print(len(paths))
