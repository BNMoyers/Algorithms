#!/usr/bin/python

import math

  #first pass notes
  #check that both dicts have the same keys
  #loop through the recipe and ingredient dictionaries, comparing values
  # if any vallue in ingredients is less than the corresponding recipe amount, exit the loop and return 0
  # divide each ingredient by the amount in recipe; drop the remainder, push to list
  # return the shortest amount found in list
def recipe_batches(recipe, ingredients):
  if recipe.keys() != ingredients.keys():
    return 0
  
  batch_compare = []
  
  for key in recipe.keys():
    
      batch_compare.append(ingredients[key] // recipe[key])
  
  min = batch_compare[0]
  for i in batch_compare:
    if i < min:
      min = i
  return min

  batches = min
  return batches



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))