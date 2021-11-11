# Py2 builds on the previous challenges and adds the use of functions with parameters

'''
  All challenges in this repository are seperated into four levels: Foundation, Intermediate, Advanced and Expert.
  The expectation is to complete all Foundation level challenges, with Intermediate and upwards pushing your knowledge
  and may require you to google things in order to solve them. If you find an answer online somewhere, be kind and
  share it with the group!
'''

'''
 # A function that concatenates two strings together with a space in between them.
 #
 # @param {string} firstName John
 # @param {string} lastName Smith
 # @returns {string} John Smith
'''
def createFullName(firstName, lastName):  
  fullName = firstName + " " + lastName
  return fullName

'''
 # A function that takes two numbers as an input and returns the smallest one.
 # !!NOTE!! You'll have to write in the parameters for this function yourself.
 # Should return "They are equal" if the numbers are the same
 #
 # @param {number} number1 100
 # @param {number} number2 200
 # @returns {number} 100
'''
def findSmallestNumber(number1, number2):
  if(number1 < number2):
    return number1
  elif(number2 < number1):
    return number2
  elif(number1 == number2):
    return "They are equal"

'''
 # A function that takes two numbers as input, multiplies them together and returns the product.
 # !!NOTE!! You'll have to write in the parameters for this function yourself.
 #
 # @param {number} number1 3
 # @param {number} number2 6
 # @returns {number} 18
'''
def multiplyNumbers(number1, number2):
  return number1*number2