from random import randint

class dice:
  def __init__(self, sides):
    self.sides = sides
    self.result = 0

  def roll(self):
    self.result = randint(1, self.sides)
    return self.result

  def lastResult(self):
    return self.result

