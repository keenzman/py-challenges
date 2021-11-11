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

if __name__ == '__main__':
  unittest.main()