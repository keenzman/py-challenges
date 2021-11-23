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



 
