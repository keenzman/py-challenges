'''
  Py4 builds on the previous challenges and adds the use of Array iterators, Arrays, For Loops, Conditionals (If, else, switch)
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
 # A function that takes an array of Booleans and then removes the false values from the given array.
 # It should create a new array only consiting of the true values.
 #
 # @param {boolean[]} booleanArr [true, true, false, false, true]
 # @return {boolean[]} [true, true, true]
'''
def removeFalseValues(booleanArr):
  filter_list = list(filter(lambda value: value == True, booleanArr))
  return filter_list

'''
 # A function that takes an array of numbers that are between 0 - 1.
 # The function needs to create a new array with the numbers converted into a percentage
 #
 # @param {number[]} numbersArr [1, .5, .7, .25]
 # @return {string[]} ["100%", "50.0%", "70.0%", "25.0%"]
'''
def createPercentageList(numbersArr):
  map_list = list(map(lambda value: f'{value * 100}%', numbersArr))
  return map_list

'''
 # A function that takes an array of possessions and a name.
 # The functions needs to create a new array with the name prefixed to each item.
 #
 # @param {string[]} possessionsArr ["shoes", "jacket", "belt"]
 # @param {string} name "disco"
 # @return {string[]} ["disco shoes", "disco jacket", "disco belt"]
'''
def createListOfPoessessions(possessionsArr, name):
  map_possessions = list(map(lambda possession: f'{name + " " + possession}', possessionsArr))
  return map_possessions

''' Intermediate Challenges '''

'''
 # A function that takes a string of numbers joined with a "+" and returns an array of those numbers.
 # The strings will need to be converted into numbers.
 # e.g 1 instead of "1"
 #
 # @param {string} numberString - "1+2+3+4+5"
 # @return {number[]} [1, 2, 3, 4, 5]
'''
def convertStringToNumbersArray(numberString):
  splitList = numberString.split("+")
  convertedNumList = ([int(num) for num in splitList])
  return convertedNumList

'''
 # A function that takes a string of numbers joined with a "+" and creates a new array based on if the number is even or odd.
 # Every number in the string will need to checked.
 #
 # @param {string} numberString - "1+2+3+4+5"
 # @return {string[]} ['odd', 'even', 'odd', 'even', 'odd']
'''
def createOddEvenArray(numberString):
  splitList = numberString.split("+")
  convertedNumList = ([int(num) for num in splitList])
  map_Nums = list(map(lambda num: f'even' if (num%2==0) else f'odd', convertedNumList))
  return map_Nums

'''
 # A function that takes an array of book titles and a search term.
 # The function needs fo remove any book titles that do not include the search term.
 #
 # @param {string[]} booksArr ["JavaScript: The Definitive Guide", "JavaScript: The Good Parts", "The Google story", "React for Dummies"]
 # @param {string} - searchTerm - "Google"
 # @return {string[]} - ["The Google story"]
'''
def filterBooksBySearch(booksArr, searchTerm):
  filter_books = list(filter(lambda book: searchTerm in book, booksArr))
  return filter_books