''' This challenge introduces the use of Set, String, Tuple and Dictionary '''

'''
  All challenges in this repository are seperated into four levels: Foundation, Intermediate, Advanced and Expert.
  The expectation is to complete all Foundation level challenges, with Intermediate and upwards pushing your knowledge
  and may require you to google things in order to solve them. If you find an answer online somewhere, be kind and
  share it with the group!
'''

''' Foundation Challenges '''

'''
  # Return a new set of identical numbers from two sets
  # @params {set1}, {set2}
  # @returns {set}
'''
def identicalItems(set1, set2):
  identifyItems = set1.intersection(set2)
  return identifyItems
