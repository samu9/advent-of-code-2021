import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--day', action='store')
parser.add_argument('--part', action='store')

args = parser.parse_args()
__import__(f"aoc.day_{args.day}.part{args.part}")