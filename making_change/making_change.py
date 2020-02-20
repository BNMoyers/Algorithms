#!/usr/bin/python

import sys

# should work a lot like eating cookies, except instead of 3 we're working with 5, and the values of each option are not sequential
# will need to figure out if the amount is higher than a given denomination; we can safely ignore all higher denominations for that number
# definitely need a cache 


def making_change(amount, denominations):
  cache = [0 for i in range(amount +1)]
  cache[0] = 1
  
  if amount < 0:
   return 0
  
  if amount == 0 or amount == 1:
    return 1
  
  elif cache[amount] > 0:
    return cache[amount]
  
  else:
    for coin in denominations:
      for biggest in range(coin, amount +1):
        difference = biggest - coin
        if difference >=0:
          cache[biggest] += cache[difference]
    return cache[amount]


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")