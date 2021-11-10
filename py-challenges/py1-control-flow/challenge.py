''' This challenge is designed to test you knowledge of Types and Control Flow (If and Switch Statements) '''

''' 
  All challenges in this repository are seperated into four levels: Foundation, Intermediate, Advanced and Expert.
  The expectation is to complete all Foundation level challenges, with Intermediate and upwards pushing your knowledge
  and may require you to google things in order to solve them. If you find an answer online somewhere, be kind and
  share it with the group!
'''

''' Foundation Challenges '''

'''
 * A function that programmatically concatenates two strings together with a space in between them.
 * This means if the string were different it would still add them together.
 *
 * @returns {string} John Smith
'''

def createFullName():
  firstName = "John"
  lastName = "Smith"
  
  return (firstName + " " + lastName)

def findLargestNumber():
  largeNum1 = 1000
  largeNum2 = 4000

  if(largeNum1 > largeNum2):
    return largeNum1
  elif(largeNum2 > largeNum1):
    return largeNum2
  elif(largeNum1 == largeNum2):
    return "They are equal"

def sumNumbers(x, y):
  
  return x + y