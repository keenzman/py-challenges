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
  return number1 * number2

''' Intermediate Challenges '''

'''
 # A function that tells the user whether or not they've achieved a new high score.
 # If they new score is larger than the current high score then return "You got a new high score!"
 # If the scores are the same return "So close!"
 # Otherwise return "Better luck next Time"
 #
 # @param {number} score 300
 # @param {number} highScore 325
 # @returns {string} "You got a new high score!" | "So close!" | "Better luck next time!"
'''
def checkIfNewHighScore(score, highScore):
  if(score > highScore):
    return "You got a new high score!"
  elif(score == highScore):
    return "So close!"
  else:
    return "Better luck next Time"

'''
 # A function that converts a temperature a in celsius to fahrenheit and outputs it in a string format -> "15 degrees celsius is 59 degrees fahrenheit".
 #
 # @param {number} tempInCelsius 15
 # @returns {string} "15 degrees celsius is 59 degrees fahrenheit"
'''
def celsiusToFahrenheit(tempInCelsius):
  tempInFahrenheit = (tempInCelsius * 9) // 5 + 32
  temperatureString = f"{tempInCelsius} degrees celsius is {tempInFahrenheit} degrees fahrenheit"
  return temperatureString

'''
 # A function that calculates the number of snickers needed for the rest of your life based on the number you eat per day,
 # your age and your maximum age.
 #
 # @param {number} snickersPerDay 2
 # @param {number} age 25
 # @param {number} maxAge 100
 # @returns {number} 54750
'''
def calculateLifetimeSupply(snickersPerDay, age, maxAge):
  snickersPerYear = snickersPerDay * 365
  yearsLeft = maxAge - age

  return snickersPerYear * yearsLeft