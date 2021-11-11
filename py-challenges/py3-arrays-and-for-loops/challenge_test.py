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


if __name__ == '__main__':
  unittest.main()