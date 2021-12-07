from functools import reduce
import statistics

with open("aoc/day_7/input.txt") as fp:
    input_ = fp.read().splitlines()

positions = list(map(int, input_[0].split(',')))

def move_cost(steps):
    return (steps * (steps + 1))/2

min_cost = min(map(lambda i: reduce(lambda x,y: x + y, map(lambda p: move_cost(abs(p - i)), positions)), range(max(positions))))

print(min_cost)
