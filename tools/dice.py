from random import randint

class dice:
  def __init__(self, sides):
    self.sides = sides
    self.result = 0

  def roll(self):
    self.result = randint(1, self.sides)
    return self.result

  def dropLowest(self, rolls=4):
    rollList = [self.roll() for i in range(rolls)]
    rollList.remove(min(rollList))
    return sum(rollList)

  def dropHighest(self, rolls=4):
    rollList = [self.roll() for i in range(rolls)]
    rollList.remove(max(rollList))
    return sum(rollList)

  def lastResult(self):
    return self.result

