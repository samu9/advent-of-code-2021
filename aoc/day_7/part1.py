from os import stat
import statistics

with open("aoc/day_7/input.txt") as fp:
    input_ = fp.read().splitlines()

positions = list(map(int, input_[0].split(',')))
median = statistics.median(positions)
movement = sum(map(lambda p: abs(p - median), positions))

print(movement)
