with open("aoc/day_2/input.txt") as fp:
    input_ = fp.read().splitlines()

horizontal = 0
depth = 0
aim = 0

for i in input_:
    command, val = i.split(" ")
    val = int(val)
    if command == "forward":
        horizontal += val
        depth += aim * val
    if command == "down":
        aim += val
    if command == "up":
        aim -= val

print(horizontal, depth)
print(horizontal * depth)