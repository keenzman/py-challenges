''' This challenge is designed to test you knowledge of Types and Control Flow (If and Switch Statements) '''

''' 
  All challenges in this repository are seperated into four levels: Foundation, Intermediate, Advanced and Expert.
  The expectation is to complete all Foundation level challenges, with Intermediate and upwards pushing your knowledge
  and may require you to google things in order to solve them. If you find an answer online somewhere, be kind and
  share it with the group!
'''

''' Foundation Challenges '''

'''
 # A function that programmatically concatenates two strings together with a space in between them.
 # This means if the string were different it would still add them together.
 #
 # @returns {string} John Smith
'''
firstName = "John"
lastName = "Smith"

def createFullName():  
  return (firstName + " " + lastName)

'''
 # A function that programmatically returns the largest number.
 # This means if the numbers were different it would still return the largest one.
 #
 # @returns {number} the largest number
'''
largeNum1 = 1000
largeNum2 = 4000

def findLargestNumber():
  if(largeNum1 > largeNum2):
    return largeNum1
  elif(largeNum2 > largeNum1):
    return largeNum2
  elif(largeNum1 == largeNum2):
    return "They are equal"

def sumNumbers(x, y):
  return x + y

''' Intermediate Challenges '''

'''
 # A function to programmatically find the length of a string.
 # This means if the string was different it would still find the length.
 #
 # BONUS: Try to solve this without using any built-in methods
 #
 # @returns {number} the length of the string
'''
password = "thisIsMyVeryLongPassword123456789";

def findLengthOfPassword(password):
  counter = 0
  for i in password:
    counter += 1
  return counter