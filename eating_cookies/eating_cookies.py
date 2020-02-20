#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

#first pass notes:
# if < 0 return 0, else set base case of 0 or 1 to 1.
# save smaller answers in the cache, to speed things up by referring to them later
# check if answer is in cache, else run loop
# add together possible combos and pass to the cache
# return n from cache, rinse and repeat
def eating_cookies(n, cache=None):
  if n < 0:
    return 0
  
  elif n == 0 or n == 1:
    return 1

  elif cache and cache[n] >0:
    return cache[n]

  else:
    if cache is None:
      cache = {}
    cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    return cache[n]

  
  


  

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')