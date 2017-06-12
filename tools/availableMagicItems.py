from dice import dice

class community:
  diceBag = { '100': dice(100), '20': dice(20), '10': dice(10), '8': dice(8), '6': dice(6), '4': dice(4) }
  minor = medium = major = 0

  def __init__(self, size):
    self.size = size
    getattr(self, '_' + self.__class__.__name__ + '__' + size)()
  
  def __Thorp(self):
    self.baseValue = 50
    self.minor = self.diceBag['4'].roll()

  def __Hamlet(self):
    self.baseValue = 200
    self.minor = self.diceBag['6'].roll()

  def __Village(self):
    self.baseValue = 500
    self.minor = self.diceBag['4'].roll() + self.diceBag['4'].roll()
    self.medium = self.diceBag['4'].roll()

  def __SmallTown(self):
    self.baseValue = 1000
    self.minor = self.diceBag['4'].roll() + self.diceBag['4'].roll() + self.diceBag['4'].roll()
    self.medium = self.diceBag['6'].roll()

  def __LargeTown(self):
    self.baseValue = 2000
    self.minor = self.diceBag['4'].roll() + self.diceBag['4'].roll() + self.diceBag['4'].roll()
    self.medium = self.diceBag['4'].roll() + self.diceBag['4'].roll()
    self.major = self.diceBag['4'].roll()

  def __SmallCity(self):
    self.baseValue = 4000
    self.minor = self.diceBag['4'].roll() + self.diceBag['4'].roll() + self.diceBag['4'].roll() + self.diceBag['4'].roll()
    self.medium = self.diceBag['4'].roll() + self.diceBag['4'].roll() + self.diceBag['4'].roll()
    self.major = self.diceBag['6'].roll()

  def __LargeCity(self):
    self.baseValue = 8000
    self.minor = self.diceBag['4'].roll() + self.diceBag['4'].roll() + self.diceBag['4'].roll() + self.diceBag['4'].roll()
    self.medium = self.diceBag['4'].roll() + self.diceBag['4'].roll() + diceBag['4'].roll()
    self.major = self.diceBag['4'].roll() + self.diceBag['4'].roll()

  def __Metropolis(self):
    self.baseValue = 16000
    self.medium = self.diceBag['4'].roll() + self.diceBag['4'].roll() + self.diceBag['4'].roll() + self.diceBag['4'].roll()
    self.major = self.diceBag['4'].roll() + self.diceBag['4'].roll() + self.diceBag['4'].roll()

  def get(self):
    return [self.size, self.baseValue, self.minor, self.medium, self.major]

  def prettyPrint(self):
    print 'Size: %s\nBase Value: %d\nMinor: %d\nMedium: %d\nMajor: %d' % (self.size, self.baseValue, self.minor, self.medium, self.major)
