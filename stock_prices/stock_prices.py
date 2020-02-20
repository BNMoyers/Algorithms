#!/usr/bin/python

import argparse
#iterate through the price list
#hold the highest and lowest number separately
#hold the current profit margin in temp variable, update only when higher -- problem: this doesn't account for negative numbers; fix by setting profit to the first possible profit margin, rather than 0.
#when there is a new low number, set it to both variables (so that you're only comparing possible profits that come after )
def find_max_profit(prices):
  high = prices[0]
  low = prices[0]
  profit = prices[1] - prices[0]

  for i in prices:
    if i < low:
     high = i
     low = i
    elif i > high:
      high = i
      profit = high - low
  return profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))