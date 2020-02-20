#!/usr/bin/python

import sys

# make a list of all possible moves
# hints suggest using a helper function to do the recursion
# need to iterate over moves and create combos based on n
# check length and return easy answer first if possible
# otherwise, decrement a temporary array and concat each possible move to get a sub list
# append the sublist to the final list and return
def rock_paper_scissors(n):
  moves = [["rock"], ["paper"], ["scissors"]]
  plays = []

  if n < 1:
    return [[]]

  if n == 1:
    return moves

  tempArr = rock_paper_scissors(n-1)

  for subArr in tempArr:
    for move in moves:
      addedMove = subArr + move
      plays.append(addedMove)
  return plays


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')