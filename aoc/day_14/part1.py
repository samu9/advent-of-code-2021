from utils import read_input

input_ = read_input(__file__)

pattern = input_[0]

rules = input_[2:]


def insert(rule: str, pattern: str) -> str:
    bigram, letter = rule.split(" -> ")

    if bigram not in pattern:
        return pattern

    index = pattern.find(bigram)
    pattern = pattern[:index + 1] + letter + pattern[index + 1:]

    return pattern


for i in range(10):
    for r in rules:
        pattern = insert(r, pattern)

letters = {p: pattern.count(p) for p in {*pattern}}
sorted_occurences = list(letters.values())
sorted_occurences.sort(reverse=True)
print(sorted_occurences[0] - sorted_occurences[-1])
