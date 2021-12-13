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

  def test_Circle(self):
    areaOfCircle = challenge.Circle(2).getArea()
    self.assertEqual(areaOfCircle, 12.56)

    circumferenceOfCircle = challenge.Circle(2).getCircumference()
    self.assertEqual(circumferenceOfCircle, 12.56)

  def test_seating_capacity(self):
    School_bus = challenge.Bus("School Volvo", 180, 12)
    checkCapacity = School_bus.seating_capacity()
    self.assertEqual(checkCapacity, 'The seating capacity of a School Volvo is 50 passengers')

  def test_deposit(self):
    bank_balance = challenge.BankAccount()
    depositMoney = bank_balance.deposit(1000)
    self.assertEqual(depositMoney, 1000)
  
  def test_withdraw(self):
    bank_balance = challenge.BankAccount()
    withdrawMoney = bank_balance.withdraw(100)
    self.assertEqual(withdrawMoney, -100)

    min_balance = 100
    bank_balance = challenge.MinimumBalanceAccount(min_balance)
    withdrawMoney = bank_balance.withdraw(100)
    self.assertEqual(withdrawMoney, 'Sorry, minimum balance must be maintained.')

  
if __name__ == '__main__':
  unittest.main()