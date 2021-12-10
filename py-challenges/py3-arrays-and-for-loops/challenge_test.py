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

  def test_removeEvenNumbers(self):
    numList = [1,1,8,1,1,8]
    self.assertEqual(challenge.removeEvenNumbers(numList), [1,1,1,1])

    numList2 = [2]
    self.assertEqual(challenge.removeEvenNumbers(numList2), [])

    numList3 = [1]
    self.assertEqual(challenge.removeEvenNumbers(numList3), [1])

  def test_generateAverage(self):
    numList = [1,2,3]
    self.assertEqual(challenge.generateAverage(numList), 2)

    numList2 = [1, 2, 3, 4, 5, 6]
    self.assertEqual(challenge.generateAverage(numList2), 4)

    numList3 = [50, 60, 30, 70]
    self.assertEqual(challenge.generateAverage(numList3), 52)

  def test_reverseOrder(self):
    reverseList = [1, 2, 3]
    self.assertEqual(challenge.reverseOrder(reverseList), [3,2,1])

    reverseList2 = ["A", "B", "C"]
    self.assertEqual(challenge.reverseOrder(reverseList2), ["C", "B", "A"])

    reverseList3 = [3]
    self.assertEqual(challenge.reverseOrder(reverseList3), [3])

    reverseList3 = []
    self.assertEqual(challenge.reverseOrder(reverseList3), [])

  def test_generateHighscores(self):
    players = ["Andy", "Bex", "Calum"]
    playerScores = [60, 99, 71]
    highscores = ["P:1 Andy scored 60", "P:2 Bex scored 99", "P:3 Calum scored 71"]

    self.assertEqual(challenge.generateHighscores(players, playerScores), highscores)

    players2 = ["Tony","John","Dave"]
    playerScores2 = [45,55,66]
    highscores2 = ["P:1 Tony scored 45","P:2 John scored 55","P:3 Dave scored 66"]
    
    self.assertEqual(challenge.generateHighscores(players2, playerScores2), highscores2)

    players3 = ["Tony"]
    playerScores3 = [45]
    highscores3 = ["P:1 Tony scored 45"]
    
    self.assertEqual(challenge.generateHighscores(players3, playerScores3), highscores3)

if __name__ == '__main__':
  unittest.main()