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