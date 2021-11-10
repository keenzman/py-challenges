import unittest
import challenge

class ControlFlowTest(unittest.TestCase):

  def test_createFullName(self):
    result = challenge.createFullName()
    self.assertIn(result, "John Smith")

if __name__ == '__main__':
  unittest.main()