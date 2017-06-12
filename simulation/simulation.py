import sys, os
from character import character
from classes import classes
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'tools'))
from dice import dice

characterList = []
diceBag = { '20': dice(20), '10': dice(10), '8': dice(8), '6': dice(6), '4': dice(4) }
Classes = classes()

def constructCharacters():
  characterAmount = input('How many characters do you want to create? ')
  for i in range(characterAmount):
    characterList.append(
	character(
	  diceBag['6'].roll() + diceBag['6'].roll() + diceBag['6'].roll(), 
	  diceBag['6'].roll() + diceBag['6'].roll() + diceBag['6'].roll(), 
	  diceBag['6'].roll() + diceBag['6'].roll() + diceBag['6'].roll(), 
	  diceBag['6'].roll() + diceBag['6'].roll() + diceBag['6'].roll(), 
	  diceBag['6'].roll() + diceBag['6'].roll() + diceBag['6'].roll(), 
	  diceBag['6'].roll() + diceBag['6'].roll() + diceBag['6'].roll()
	  )
	)
    characterClass = raw_input('What class do you want character %d to have? ' % (i + 1))
    characterList[i].addClass(characterClass, Classes.getClass(characterClass))
    

if __name__ == '__main__':
  constructCharacters()
  for i in characterList: print i.Abilities, i.Class
