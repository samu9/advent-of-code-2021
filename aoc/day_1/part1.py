with open("day_1/input.txt") as fp:
    input_ = list(map(lambda val: int(val), fp.read().splitlines()))

increases = 0
previous = input_[0]

for i in input_:
    if i > previous:
        increases += 1
    previous = i

print(increases)