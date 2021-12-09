import unittest
from unittest import result
import challenge

class ControlFlowTest(unittest.TestCase):

  def test_createFullName(self):
    result = challenge.createFullName()
    self.assertIn(result, "John Smith")

  def test_findLargestNumber(self):
    result = challenge.findLargestNumber()
    self.assertEqual(result, 4000)

    largeNum1 = 1000
    largeNum2 = 1000
    message = 'They should be equal'
    self.assertEqual(largeNum1, largeNum2, message)

  def test_sumNumbers(self):
    self.assertEqual(challenge.sumNumbers(10, 20), 30)  
    self.assertEqual(challenge.sumNumbers(-1, 1), 0)
    self.assertEqual(challenge.sumNumbers(-1, -1), -2)

  def test_findLengthOfPassword(self):
    password1 = "thisIsMyVeryLongPassword123456789"
    self.assertEqual(challenge.findLengthOfPassword(password1), 33)

    password2 = "password123"
    self.assertEqual(challenge.findLengthOfPassword(password2), 11)

  def test_findType(self):
    thing = "I am a thing"
    message = "This is a string"
    self.assertIn(challenge.findType(thing), message)

    thing = 123
    message = "This is a number"
    self.assertIn(challenge.findType(thing), message)

    thing = True
    message = "This is a boolean"
    self.assertIn(challenge.findType(thing), message)

    thing = False
    message = "This is a boolean"
    self.assertIn(challenge.findType(thing), message)

  def test_getIsValidOnNameTag(self):
    result = challenge.getIsValidOnNameTag()
    self.assertEqual(result, True)

  def test_convertStringToNumber(self):
    result = challenge.convertStringToNumber()
    self.assertEqual(result, 15.45)

  def test_getHasUppercaseLetters(self):
    result = challenge.getHasUppercaseLetters()
    self.assertEqual(result, True)

  def test_convertPascalCaseToSnakeCase(self):
    result = challenge.convertPascalCaseToSnakeCase()
    self.assertEqual(result, "i_want_to_be_snake_case")

if __name__ == '__main__':
  unittest.main()