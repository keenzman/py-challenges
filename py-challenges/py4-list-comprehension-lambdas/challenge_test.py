import unittest
import challenge

class ControlFlowTest(unittest.TestCase):

  def test_removeFalseValues(self):
    booleanList = [True, True, False, False, True]
    result = challenge.removeFalseValues(booleanList)
    self.assertEqual(result, [True, True, True])

    booleanList2 = [False, False]
    result = challenge.removeFalseValues(booleanList2)
    self.assertEqual(result, [])

  def test_createPercentageList(self):
    numberArr = [1, .5, .7, .25]
    result = challenge.createPercentageList(numberArr)
    self.assertEqual(result, ["100%", "50.0%", "70.0%", "25.0%"])

    numberArr2 = [.25]
    result = challenge.createPercentageList(numberArr2)
    self.assertEqual(result, ["25.0%"])

  def test_createListOfPoessessions(self):
    possessionsList = ["shoes", "jacket", "belt"]
    result = challenge.createListOfPoessessions(possessionsList, "disco")
    self.assertEqual(result, ["disco shoes","disco jacket","disco belt"])

  def test_convertStringToNumbersArray(self):
    numString = "1+2+3+4+5"
    result = challenge.convertStringToNumbersArray(numString)
    self.assertAlmostEqual(result, [1, 2, 3, 4, 5])

  def test_createOddEvenArray(self):
    numString = "1+2+3+4+5"
    result = challenge.createOddEvenArray(numString)
    self.assertAlmostEqual(result, ['odd', 'even', 'odd', 'even', 'odd'])

  def test_filterBooksBySearch(self):
    bookList = ["JavaScript: The Definitive Guide", "JavaScript: The Good Parts", "The Google story", "React for Dummies"]
    searchTerm = "Google"
    result = challenge.filterBooksBySearch(bookList, searchTerm)
    self.assertAlmostEqual(result, ["The Google story"])

    searchTerm2 = "JavaScript"
    result = challenge.filterBooksBySearch(bookList, searchTerm2)
    self.assertAlmostEqual(result, ["JavaScript: The Definitive Guide", "JavaScript: The Good Parts"])

    searchTerm3 = "Python"
    result = challenge.filterBooksBySearch(bookList, searchTerm3)
    self.assertAlmostEqual(result, [])

if __name__ == '__main__':
  unittest.main()