from functools import reduce

with open("aoc/day_3/input.txt") as fp:
    input_ = fp.read().splitlines()

bits = list(map(lambda i: [int(char) for char in i], input_))
sum_ = reduce(lambda x, y: [x[i]+ v for i, v in enumerate(y)], bits, [0] * len(bits[0]))
gamma = int("".join(list(map(lambda s: str(int(s > len(bits)/2)), sum_))),2)
epsilon = int("".join(list(map(lambda s: str(int(s < len(bits)/2)), sum_))),2)

print(gamma * epsilon)