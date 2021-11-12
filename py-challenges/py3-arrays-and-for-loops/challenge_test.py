import unittest
import challenge

class ControlFlowTest(unittest.TestCase):

  def test_createRecipeString(self):
    ingredientsArr = ["Bacon","Lettuce","Tomato"]
    result = challenge.createRecipeString(ingredientsArr)
    self.assertEqual(result, "Bacon+Lettuce+Tomato")

    self.assertEqual(type(challenge.createRecipeString(ingredientsArr)), str)

    self.assertEqual(challenge.createRecipeString(["Chicken"]), "Chicken")

  def test_getFirstAndLastItems(self):
    itemsArr = ["Tony","John","Dave"]
    self.assertEqual(challenge.getFirstAndLastItems(itemsArr), ["Tony","Dave"])

  def test_totalScores(self):
    scoreArr = [1,2,3]
    self.assertEqual(challenge.totalScores(scoreArr), 6)

    self.assertEqual(type(challenge.totalScores(scoreArr)), int)

    self.assertEqual(challenge.totalScores([10]), 10)

  def test_totalRange(self):
    self.assertEqual(challenge.totalRange(1), 1)
    self.assertEqual(challenge.totalRange(10), 55)
    self.assertEqual(challenge.totalRange(2000), 2001000)

  def test_moveFirstAndLastItems(self):
    itemsArr = ["Pear","Apple","Orange"]
    self.assertEqual(challenge.moveFirstAndLastItems(itemsArr), ["Orange","Pear","Apple"])

    itemsArr2 = ["Pear"]
    self.assertEqual(challenge.moveFirstAndLastItems(itemsArr2), ["Pear"])

  def test_generateAverage(self):
    numList = [1,1,8,1,1,8]
    self.assertEqual(challenge.generateAverage(numList), [1,1,1,1])

    numList2 = [2]
    self.assertEqual(challenge.generateAverage(numList2), [])

    numList3 = [1]
    self.assertEqual(challenge.generateAverage(numList3), [1])

if __name__ == '__main__':
  unittest.main()