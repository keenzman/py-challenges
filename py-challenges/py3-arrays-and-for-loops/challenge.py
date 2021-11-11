'''
  Py3 builds on the previous challenges and adds the use of Arrays, For Loops, Conditionals (If, else, switch)
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
 # A function that creates a a Recipe string from a given array of Ingredients.
 # Each ingredient will be joined with a +.
 #
 # @param {string[]} ingredientsArr ["Bacon","Lettuce","Tomato"]
 # @return {string} "Bacon+Lettuce+Tomato"
'''
def createRecipeString(ingredientsArr):
  recipe = '+'.join(ingredientsArr)
  return recipe 

'''
 # A function that takes Array of Items and returns a NEW ARRAY with the first and last item in it.
 #
 # @param {string[]} itemsArr ["Tony","John","Dave"]
 # @return {string[]} ["Tony","Dave"]
'''
def getFirstAndLastItems(itemsArr):
  firstItem = itemsArr[0]
  lastItem = itemsArr[-1]
  newItemsArray = [firstItem, lastItem]
  return newItemsArray

'''
 # A function that takes an array of scores and totals the scores by looping through the array.
 #
 # @param {number[]} scoreArr [1,2,3]
 # @return {number} 6
'''
def totalScores(scoreArr):
  total = 0
  for score in scoreArr:
    total += score
  return total