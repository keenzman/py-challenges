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


if __name__ == '__main__':
  unittest.main()