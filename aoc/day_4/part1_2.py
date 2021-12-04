
from typing import Dict, List
from functools import reduce

with open("aoc/day_4/input.txt") as fp:
    input_ = fp.read().splitlines()

class Board:
    matrix: List[int]
    signed: List[bool]
    width: int
    height: int

    rounds_played = 0
    victory_number = None

    def __init__(self, input_, width, height) -> None:
        self.width = width
        self.height = height
        self.matrix =input_
        self.signed = [False] * len(input_)
        self.horizontal_checks = list(map(lambda i: sum(range(self.width * i +1, self.width * (i+1) + 1)), range(self.height)))
        self.vertical_checks = list(map(lambda i: sum(range(i +1, self.width ** 2 + i +1, self.width)), range(self.height)))

    def sign(self, num):
        self.signed[self.matrix.index(num)] = True

    def search(self, num):
        return num in self.matrix

    def sum_unmarked(self):
        return sum([x for i, x in enumerate(self.matrix) if not self.signed[i]])

    def check(self):
        horizontal_signs = list(map(lambda i: sum([x+1 for x in range(self.width * i, self.width * (i+1)) if self.signed[x]]), range(self.height)))
        vertical_signs = list(map(lambda i: sum([x+1 for x in range(i, self.width **2 + i, self.width) if self.signed[x]]), range(self.height)))
        return any([x==self.horizontal_checks[i] for i, x in enumerate(horizontal_signs)]) or any([x==self.vertical_checks[i] for i,x in enumerate(vertical_signs)])

    def play(self, draws):
        for i, d in enumerate(draws):
            if self.search(d):
                self.sign(d)
                if self.check():
                    self.rounds_played = i + 1
                    self.victory_number = d
                    return


draws = list(map(int,input_[0].split(',')))
boards = []

current = []
width = len(input_[2].split())
height = 0
for idx, i in enumerate(input_[2:]):
    if i == '':
        board = Board(current, width, height)
        board.play(draws)
        boards.append(board)
        current = []
        height = 0
    else:
        current.extend(list(map(int, i.split())))
        height += 1

rounds = list(map(lambda b: b.rounds_played, boards))
winner = boards[rounds.index(min(rounds))]
last_winner = boards[rounds.index(max(rounds))]
print(winner.victory_number * winner.sum_unmarked())
print(last_winner.victory_number * last_winner.sum_unmarked())