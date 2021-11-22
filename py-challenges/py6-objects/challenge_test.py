import unittest
import challenge

class ControlFlowTest(unittest.TestCase):

  def test_getFurniturePrice(self):
    furnitureCatalogue = challenge.Catalogue()
    furniture = furnitureCatalogue.getFurniturePrice("Table", 6)
    self.assertEqual(furniture, 6)

  def test_setFurnitureStoreLocation(self):
    furnitureCatalogue = challenge.Catalogue()
    furniture = furnitureCatalogue.setFurnitureStoreLocation("Table", 6, "Cardiff")
    self.assertEqual(furniture, "Cardiff")

if __name__ == '__main__':
  unittest.main()