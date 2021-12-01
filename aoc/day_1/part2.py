with open("day_1/input.txt") as fp:
    input_ = list(map(lambda val: int(val), fp.read().splitlines()))

increases = 0
previous = None
sum_ = 0

for idx, i in enumerate(input_):
    sum_ += i
    if idx < 3:
        if idx == 2:
            previous = sum_
        continue
    sum_ -= input_[idx-3]
    if sum_ > previous:
        increases += 1
    previous = sum_

print(increases, sum_)