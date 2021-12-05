import unittest
import challenge

class AdvancedDataTypeTest(unittest.TestCase):

  def test_identicalItems(self):
    firstSet = {10, 20, 30, 40, 50}
    secondSet = {30, 40, 50, 60, 70}
    result = challenge.identicalItems(firstSet, secondSet)
    self.assertEqual(result, {40, 50, 30})

    firstSet = {20, 30, 40}
    secondSet = {30, 40, 50, 60, 70}
    result = challenge.identicalItems(firstSet, secondSet)
    self.assertEqual(result, {40, 30})

if __name__ == '__main__':
  unittest.main()