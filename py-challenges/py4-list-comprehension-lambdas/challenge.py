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