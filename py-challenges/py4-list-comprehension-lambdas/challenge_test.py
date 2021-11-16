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


if __name__ == '__main__':
  unittest.main()