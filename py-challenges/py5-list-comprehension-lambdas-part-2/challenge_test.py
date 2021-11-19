import unittest
import challenge

class ControlFlowTest(unittest.TestCase):

  def test_totalScoresArr(self):
    numList = [7, 7, 6, 2, 3, 2, 3]
    result = challenge.totalScoresArr(numList)
    self.assertEqual(result, 30)

    numList2 = [3]
    result = challenge.totalScoresArr(numList2)
    self.assertEqual(result, 3)

  def test_reverseString(self):
    stringToReverse = "reverse this"
    result = challenge.reverseString(stringToReverse)
    self.assertEqual(result, "siht esrever")

    stringToReverse2 = "r"
    result = challenge.reverseString(stringToReverse2)
    self.assertEqual(result, "r")

  def test_sortCharactersAlphabetically(self):
    charsArr = ["X", "B", "B", "b", "g", "l", "n", "x"]
    result = challenge.sortCharactersAlphabetically(charsArr)
    self.assertEqual(result, ["b", "b", "b", "g", "l", "n", "x", "x"])

    charsArr = ["x"]
    result = challenge.sortCharactersAlphabetically(charsArr)
    self.assertEqual(result, ["x"])

  def test_sortNumbersHighToLow(self):
    numArr = [6, 9, 55, 2, 9190, .5]
    result = challenge.sortNumbersHighToLow(numArr)
    self.assertEqual(result, [9190, 55, 9, 6, 2, 0.5])

    numArr2 = [40]
    result = challenge.sortNumbersHighToLow(numArr2)
    self.assertEqual(result, [40])

  def test_checkItemInstock(self):
    toCheck = "apple"
    message = f'{toCheck} is in stock, it is on aisle 0'
    result = challenge.checkItemInstock(toCheck)
    self.assertEqual(result, message)

    self.assertEqual(type(challenge.checkItemInstock(toCheck)), str)

    # toCheck2 = "pepper"
    # result = challenge.checkItemInstock(toCheck2)
    # self.assertEqual(result, f'Sorry {toCheck2} is not in stock') 
    # with self.assertRaises(ValueError):
    #   print('Pepper is not in list!')

  def test_checkPrimaryColours(self):
    coloursList = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    result = challenge.checkPrimaryColours(coloursList)
    self.assertEqual(result, False)

    coloursList2 = ["red", "blue", "yellow"]
    result = challenge.checkPrimaryColours(coloursList2)
    self.assertEqual(result, True)

if __name__ == '__main__':
  unittest.main()