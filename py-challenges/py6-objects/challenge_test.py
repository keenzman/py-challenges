import unittest
import challenge

class ControlFlowTest(unittest.TestCase):
  def test_getFurniturePrice(self):
    furnitureCatalogue = Catalogue()
    self.assertEqual(furnitureCatalogue.price(6), 6)

if __name__ == '__main__':
  unittest.main()