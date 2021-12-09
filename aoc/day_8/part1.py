import os
from pathlib import Path
with open(os.path.join(Path(__file__).parent, "input.txt")) as fp:
    input_ = fp.read().splitlines()

ONE_LENGTH = 2
FOUR_LENGTH = 4
SEVEN_LENGTH = 3
EIGHT_LENGTH = 7

target_lenghts = [ONE_LENGTH, FOUR_LENGTH, SEVEN_LENGTH, EIGHT_LENGTH]

occurrences = 0

for i in input_:
    signal_patterns, output_digits = i.split(' | ')
    occurrences += len(list(filter(lambda s: len(s) in target_lenghts, output_digits.split())))
print(occurrences)