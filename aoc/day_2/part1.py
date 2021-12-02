with open("aoc/day_2/input.txt") as fp:
    input_ = fp.read().splitlines()

horizontal = 0
depth = 0

for i in input_:
    command, val = i.split(" ")
    val = int(val)
    if command == "forward":
        horizontal += val
    if command == "down":
        depth += val
    if command == "up":
        depth -= val

print(horizontal, depth)
print(horizontal * depth)