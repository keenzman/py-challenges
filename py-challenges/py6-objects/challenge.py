''' This challenge build upon previous knowledge and introduces the use of objects '''

'''
  All challenges in this repository are seperated into four levels: Foundation, Intermediate, Advanced and Expert.
  The expectation is to complete all Foundation level challenges, with Intermediate and upwards pushing your knowledge
  and may require you to google things in order to solve them. If you find an answer online somewhere, be kind and
  share it with the group!
'''

'''
 # A function that takes a furniture object from the catalogue and returns its price
 #
 # furniture = {
 #  name: "lack",
 #  price: 6
 # }
 #
 # @param {{name: string, price: number}} furniture - A piece of furniture from the catalogue
 # @return {number} The price of the piece of furniture
'''
class Catalogue:
  def __init__(self, name, price):
    self.name = name
    self.price = price

  def getFurniturePrice(furniture):
    return furniture.price
