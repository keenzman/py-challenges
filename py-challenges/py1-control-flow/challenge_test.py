import unittest
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

if __name__ == '__main__':
  unittest.main()