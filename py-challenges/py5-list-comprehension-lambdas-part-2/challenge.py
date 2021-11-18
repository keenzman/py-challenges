'''
 Py5 builds on the previous challenges and adds the use of MORE Array iterators, Arrays, For Loops, Conditionals (If, else, switch)
 & calling your own functions.
'''

'''
  All challenges in this repository are seperated into four levels: Foundation, Intermediate, Advanced and Expert.
  The expectation is to complete all Foundation level challenges, with Intermediate and upwards pushing your knowledge
  and may require you to google things in order to solve them. If you find an answer online somewhere, be kind and
  share it with the group!
'''

''' Foundation Challenges '''

'''
 # A function that uses the REDUCE array iterator to total an array of scores.
 # Will need to import reduce from functools
 # The scores will be numbers.
 #
 # @param {number[]} numberArr [7, 7, 6, 2, 3, 2, 3]
 # @return {number} 30
'''
from functools import reduce

def totalScoresArr(numberArr):
  total = reduce(lambda a, b: a+b, numberArr)
  return total

'''
 # A function that reverses a string.
 # It will need to keep spaces between words.
 #
 # @param {string} toReverse "reverse this"
 # @return {string} "siht esrever"
'''
def reverseString(toReverse):
    return toReverse[::-1]

'''
 # A function that arranges an array of characters alphabetically.
 # Each character will need to be lowercase.
 # A to Z case insensitive.
 #
 # @param {string[]} charcterArr ["X", "B", "B", "b", "g", "l", "n", "x"]
 # @return {string[]} ["b", "b", "b", "g", "l", "n", "x", "x"]
'''
def sortCharactersAlphabetically(charcterArr):
  lowerCaseList = map(lambda alphabet: alphabet.lower(), charcterArr)
  return sorted(lowerCaseList)

''' Intermediate Challenges '''

'''
 # A function that arranges an array of numbers highest to the lowest number.
 #
 # @param {number[]} numberArr [6, 9, 55, 2, 9190, .5]
 # @return {number[]} [9190, 55, 9, 6, 2, 0.5]
'''
def sortNumbersHighToLow(numberArr):
  return sorted(numberArr, reverse=True)

'''
 # A function that checks if a given item is 'instock'.
 # You have been given a 'stocklist' in the function body.
 #
 # If the item is in the stocklist you need to return its index in the following string format.
 # "ITEM is instock, it is on aisle INDEX."
 #
 # If the item is not in the stocklist you need to return the following string format.
 # "Sorry ITEM is not instock."
 #
 # @param {string} toCheck orange
 # @return {string} "orange is instock, it is on aisle 2."
''' 
def checkItemInstock(toCheck):
  stockList = [
    "apple",
    "banana",
    "orange",
    "coconut",
    "strawberry",
    "lime",
    "grapefruit",
    "lemon",
    "kumquat",
    "blueberry",
    "melon",
  ]

  itemIndex = stockList.index(toCheck)
  if (itemIndex >= 0):
    message = f'{toCheck} is instock, it is on aisle {itemIndex}'
    return message 
  else:
    return f'Sorry {toCheck} is not instock';
  

