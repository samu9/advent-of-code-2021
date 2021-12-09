from utils import read_input

input_ = read_input(__file__)

ONE_LENGTH = 2
FOUR_LENGTH = 4
SEVEN_LENGTH = 3
EIGHT_LENGTH = 7


def segments_in_digit(segments, digit):
    return all(map(lambda x: x in digit, segments))


def get_segments():
    return list(filter(lambda x: x != 0, segments))


def join_segments(indexes):
    return "".join(map(lambda i: segments[i], indexes))


total = 0
for i, line in enumerate(input_):
    segments = [0] * 7
    signal_patterns, output_digits = list(map(lambda x: sorted(x.split(" ")), line.split(' | ')))

    one = next(filter(lambda x: len(x) == ONE_LENGTH, signal_patterns))
    four = next(filter(lambda x: len(x) == FOUR_LENGTH, signal_patterns))
    seven = next(filter(lambda x: len(x) == SEVEN_LENGTH, signal_patterns))
    eight = next(filter(lambda x: len(x) == EIGHT_LENGTH, signal_patterns))

    len_6_digits = filter(lambda x: len(x) == 6, signal_patterns)
    six = next(filter(lambda y: not segments_in_digit(one, y), len_6_digits))

    segments[0], = [x for x in seven if x not in one]
    segments[2], = [x for x in one if x not in six]
    segments[5], = [x for x in one if x != segments[2]]

    s4_s6 = [x for x in eight if x not in four + segments[0]]
    print(list(filter(lambda y: not (segments_in_digit(s4_s6, y)), len_6_digits)))
    nine = next()

    segments[4], = [x for x in s4_s6 if x not in nine]
    segments[6], = [x for x in s4_s6 if x != segments[4]]

    zero, = [x for x in len_6_digits if x not in [six, nine]]

    segments[1], = [x for x in zero if x not in get_segments()]
    segments[3], = [x for x in eight if x not in zero]

    two = next(filter(lambda x: all(map(lambda y: y in join_segments([0, 2, 3, 4, 6]), x)) and len(x) == 5, signal_patterns))
    three = next(filter(lambda x: all(map(lambda y: y in join_segments([0, 2, 3, 5, 6]), x)) and len(x) == 5, signal_patterns))
    five = next(filter(lambda x: all(map(lambda y: y in join_segments([0, 1, 3, 5, 6]), x)) and len(x) == 5, signal_patterns))

    digits = list(map(sorted, [zero, one, two, three, four, five, six]))

    total += int("".join(map(lambda x: str(digits.index(x)), map(sorted, output_digits))))

print(total)