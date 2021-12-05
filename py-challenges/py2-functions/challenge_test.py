import unittest
import challenge

class ControlFlowTest(unittest.TestCase):

  def test_createFullName(self):
    firstName = "John"
    lastName = "Smith"
    result = challenge.createFullName(firstName, lastName)
    self.assertIn(result, "John Smith")

  def test_findSmallestNumber(self):
    num1 = 100
    num2 = 200
    result = challenge.findSmallestNumber(num1, num2)
    self.assertEqual(result, 100)

    num1 = 1000
    num2 = 1000
    message = 'They should be equal'
    self.assertEqual(num1, num2, message)

  def test_multiplyNumber(self):
    self.assertEqual(challenge.multiplyNumbers(3, 6), 18)  
    self.assertEqual(challenge.multiplyNumbers(-1, 5), -5)
    self.assertEqual(challenge.multiplyNumbers(-1, -10), 10)

  def test_checkIfNewHighScore(self):
    self.assertEqual(challenge.checkIfNewHighScore(600, 300), "You got a new high score!")  

    score = 700
    highScore = 700
    self.assertEqual(score, highScore, "So close!")

    self.assertEqual(challenge.checkIfNewHighScore(300, 600), "Better luck next Time")  

  def test_celsiusToFahrenheit(self):
    self.assertEqual(challenge.celsiusToFahrenheit(15), "15 degrees celsius is 59 degrees fahrenheit")
    self.assertEqual(type(challenge.celsiusToFahrenheit(15)), str)

  def test_calculateLifetimeSupply(self):
    self.assertEqual(challenge.calculateLifetimeSupply(2, 25, 100), 54750)
    self.assertEqual(challenge.calculateLifetimeSupply(3, 20, 90), 76650)

  def test_getGrade(self):
    self.assertEqual(challenge.getGrade(101), "Score unavailable")
    self.assertEqual(challenge.getGrade(-10), "Score unavailable")
    self.assertEqual(challenge.getGrade(85), "A")
    self.assertEqual(challenge.getGrade(77), "B")
    self.assertEqual(challenge.getGrade(63), "C")
    self.assertEqual(challenge.getGrade(55), "D")
    self.assertEqual(challenge.getGrade(42), "E")
    self.assertEqual(challenge.getGrade(39), "F")
    

if __name__ == '__main__':
  unittest.main()