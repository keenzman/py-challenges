''' This challenge build upon previous knowledge and introduces the use of objects '''

'''
  All challenges in this repository are seperated into four levels: Foundation, Intermediate, Advanced and Expert.
  The expectation is to complete all Foundation level challenges, with Intermediate and upwards pushing your knowledge
  and may require you to google things in order to solve them. If you find an answer online somewhere, be kind and
  share it with the group!
'''

''' Foundation Challenges '''

class Catalogue():
  '''
  # A function that takes a furniture object from the catalogue and returns its price
  #
  # @param {{name: string, price: number}} furniture - A piece of furniture from the catalogue
  # @return {number} The price of the piece of furniture
  '''
  def getFurniturePrice(self, name, price):
    self.name = name
    self.price = price
    return price
  '''
  # A function to attach to a store location to a furniture object from the catalogue
  #
  # @param {{name: string, price: number}} furniture - A piece of furniture from the catalogue
  # @param {string} location - A store location to attach to a piece of furniture
  # @returns {{name: string, price: number, location: string}} furniture - A furniture object from the catalogue
  '''
  def setFurnitureStoreLocation(self, name, price, location):
    self.name = name
    self.price = price
    self.location = location
    return location

'''
# Create a Cricle class and intialize it with radius. 
# Make two methods getArea and getCircumference inside this class.
# @param radius
# @returns number
'''
class Circle():
  def __init__(self,radius):
    self.radius = radius
  def  getArea(self):
    return 3.14*self.radius*self.radius
  def getCircumference(self):
    return self.radius*2*3.14

''' Intermediate Challenges '''

'''
# Create a Bus class that inherits from the Vehicle class. 
# Give the capacity argument of Bus a default value of 50.
# @param name, max_speed, mileage
# @param capacity
# @returns string
'''
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

'''
# Create a BankAccount class that shows the balance
# Then create two methods called 'withdraw' and 'deposit'
# Each method will have the following parameters and return:
# @param amount
# @return balance
'''
class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance 

''' Advanced Challenge '''

'''
# Use the BankAccount class above to account type where the account holder has to maintain a pre-determined 
  minimum balance when withdrawing.
# @param amount
'''
class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_balance):
        BankAccount.__init__(self)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            return 'Sorry, minimum balance must be maintained.'
        else:
            return BankAccount.withdraw(self, amount)