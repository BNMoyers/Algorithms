#!/usr/bin/python

import sys

# make a list of all possible moves
# hints suggest using a helper function to do the recursion
# need to iterate over moves and create combos based on n
def rock_paper_scissors(n):
  moves = ["rock", "paper", "scissors"]
  plays = []

  return plays


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')