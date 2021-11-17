import unittest
import challenge

class ControlFlowTest(unittest.TestCase):

  def test_removeFalseValues(self):
    booleanList = [True, True, False, False, True]
    result = challenge.removeFalseValues(booleanList)
    self.assertEqual(result, [True, True, True])

if __name__ == '__main__':
  unittest.main()