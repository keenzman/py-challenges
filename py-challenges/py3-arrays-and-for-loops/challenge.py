'''
  Py3 builds on the previous challenges and adds the use of Arrays(Lists in Python), For Loops, Conditionals (If, else, switch)
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

''' Intermediate Challenges '''

'''
 # A function that takes an number and returns the total of the range of numbers between 0 and the given number.
 # e.g. 10 => 0+1+2+3+4+5+6+7+8+9+10 = 55.
 #
 # @param {number} rangeMax 10
 # @return {number} 55
'''
def totalRange(rangeMax):
  total = 0
  for num in range(rangeMax + 1):
    total += num
  return total

'''
 # A function that takes an array and returns a NEW ARRAY where the last item has been moved to the front of the array and removed from the back.
 #
 # @param {string[]} itemsArr ["Tony","John","Dave"]
 # @return {string[]} ["Dave","Tony","John"]
'''
def moveFirstAndLastItems(itemsArr):
  newArr = list(itemsArr)
  removeLastItem = newArr.pop(-1)
  newArr.insert(0, removeLastItem)
  return newArr

'''
 # A function that takes an array of numbers and returns a NEW ARRAY with only the odd numbers from the given array. It should not mutate the input array.
 #
 # @param {number[]} numberArr [1,1,8,1,1,8]
 # @return {number[]} [1,1,1,1]
'''
def removeEvenNumbers(numberArr):
  newArr = numberArr.copy()

  for number in newArr:
    if (number % 2 == 0):
      newArr.remove(number)
  return newArr

''' Advanced Challenges '''

'''
 * A function that takes an array of numbers. It returns the average from the given array.
 * The result should rounded up to the nearest decimal place.
 *
 * @param {number[]} numberArr [1,2,3]
 * @return {number} 2
'''
def generateAverage(numberArr):
  total = totalScores(numberArr)
  average = total/len(numberArr)
  return round(average);

'''
 * A function that reverses an array without using the built-in reversed().
 *
 * @param {number[]} toReverseArr [1,2,3]
 * @return {number} [3,2,1]
'''
def reverseOrder(toReverseList):
  return toReverseList[::-1]

''' Expert Challenges '''

'''
 * Given two arrays, The first being an array of players and the second being there corresponding score. Loop through them and generate a new array matching the format below.
 *
 * ["P:INDEX PLAYER scored HIGHSCORE","P:INDEX PLAYER scored HIGHSCORE","P:INDEX PLAYER scored HIGHSCORE"]
 *
 * P:INDEX will start from 1. e.g P:1 not P:0
 *
 * If the inputs are not the same size or empty return "invalid inputs"
 *
 * @param {string[]} playersArr ["Tony","John","Dave"]
 * @param {number[]} scoresArr [45,55,66]
 * @return {string[]} ["P:1 Tony scored 45","P:2 John scored 55","P:3 Dave scored 66"]
'''
def generateHighscores(playersArr, scoresArr):
  if (len(playersArr) != len(scoresArr) or not len(playersArr)): 
    return "invalid inputs"    
  scores = []
  while(len(scores) != len(playersArr)):
    index = len(scores)
    message = f'P:{index + 1} {playersArr[index]} scored {scoresArr[index]}'
    scores.append(message)
  return scores