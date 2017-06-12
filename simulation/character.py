from collections import defaultdict

class character:
  def __init__(self, Str=10, Dex=10, Con=10, Int=10, Wis=10, Cha=10):
    self.Abilities = {}
    self.Abilities['Str'] = Str
    self.Abilities['Dex'] = Dex
    self.Abilities['Con'] = Con
    self.Abilities['Int'] = Int
    self.Abilities['Wis'] = Wis
    self.Abilities['Cha'] = Cha
    self.Feats = {}
    self.Equipment = { 'Armor': {}, 'Weapons': {} }
    self.Class = { 'Level': 0, 'Class': defaultdict(int), 'Skills': [] }
    self.Skills = defaultdict(int)

  def addSkill(self, name, points=1):
    self.Skills[name] += points

  def addClass(self, name, skills, levels=1):
    self.Class['Level'] += levels
    self.Class['Class'][name] += levels
    for skill in skills:
      if skill not in self.Class['Skills']:
        self.Class['Skills'].append(skill)
