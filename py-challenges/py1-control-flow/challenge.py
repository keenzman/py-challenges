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
 # Should return "They are equal" if the numbers are the same
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

'''
 # A function that programmatically adds two numbers together.
 # This means if the numbers were different it would still add them together.
 #
 # @returns {number} the sum of both numbers
'''
num1 = 10
num2 = 20
def sumNumbers(num1, num2):
  return num1 + num2

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

'''
 # A function that programmatically tells you what the type of the variable is.
 # This variable was still one of the accepted types it would still output a string.
 # If the variable is a string output "This is a string"
 # If the variable is a number output "This is a number"
 # If the variable is a boolean output "This is a boolean"
 # If the variable is not any of those types output "I don't know what this thing is"
 #
 # @returns {string} This is a string
'''
thing = "I am a thing";

def findType(thing):
  thingType = type(thing)
  
  if (thingType == str):
    return "This is a string"
  elif(thingType == int):
    return "This is a number"
  elif(thingType == bool):
    return "This is a boolean"
  else:
    return "I don't know what this thing is"

'''
 # A function to programmatically decide if a name is suitable for a name tag.
 # This means it must still work even if the name is different and return something if name provided is incorrect.
 # Name tag rules are: The name must be less than or equal to 8 characters and begin with a capital letter.
 #
 # @returns {boolean} true || false
'''
nameTagOption = "Timothy";

def getIsValidOnNameTag():
  firstCharacter = nameTagOption[0]
  if (len(nameTagOption) <= 8 and firstCharacter.isupper()):
    return True
  else:
    return False

''' Advanced Challenges '''

'''
 # A function that programmatically converts a number stored as a string to a number type.
 # This means if the string was different it would still convert it to a number.
 #
 # @returns {number} The number converted from the string "32.87" -> 32.87
'''
stringToConvert = "15.45"

def convertStringToNumber():
  return float(stringToConvert)

'''
 # A function that uses regex to programmatically test if a string contains uppercase letters.
 # This means if the string was different it would still accurately return true or false.
 #
 # !!NOTE!! You should use regex to solve this problem! (Check out module called 're')
 #
 # @returns {boolean} true || false
'''
import re

stringWithUppercaseLetters = "I Am A String With Uppercase Letters"

def getHasUppercaseLetters():
  result = bool(re.match(r'\w*[A-Z]\w*', stringWithUppercaseLetters))
  return result

''' Expert Challenge '''

'''
 # A function that programmatically converts a string written in PascalCase to a string written in snake_case (lowercase with underscores).
 # This means if the PascalCase string changes then the function should still convert it.
 # (Might have to use re module again)
 # !!NOTE!! You should use regex to solve this problem! (Check out module called 're')
 #
 # @returns {string} i_want_to_be_snake_case
'''
pascalCaseVariableName = "IWantToBeSnakeCase"

def convertPascalCaseToSnakeCase():
  convertedName = re.sub(r'(?<!^)(?=[A-Z])', '_', pascalCaseVariableName).lower()
  return convertedName