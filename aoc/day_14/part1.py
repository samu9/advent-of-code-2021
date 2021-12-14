from typing import List
from utils import read_input

input_ = read_input(__file__)

pattern = input_[0]

rules = input_[2:]


def get_bigrams(pattern: str) -> List[str]:
    result = []
    for i in range(len(pattern) - 1):
        result.append(pattern[i:i+2])
    return result

def insert(rule: str, pattern: str) -> str:
    bigram, letter = rule.split(" -> ")

    if bigram not in pattern:
        return pattern

    index = pattern.find(bigram)
    pattern = pattern[:index + 1] + letter + pattern[index + 1:]

    return pattern

print(insert("BA -> B", "DDCCBA"))
# insert(rules[0], pattern)