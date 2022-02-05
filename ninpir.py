import random

class Ninja:
    def __init__(self, name, weapon, rank, size):
        self.name = name
        self.weapon = weapon
        self.rank = rank
        self.size = size
    
    def __repr__(self) -> str:
        return "This ninja's name is " + self.name + " and they are armed with a " + self.weapon + ". They hold the rank of " + self.rank + '.'
    
    def be_stealthy(self):
        stealthy_behaviour = ['creeping around.', 'purching up high.', 'hiding in the water.', 'pretending to be a monk.']
        print(self.name + " is " + stealthy_behaviour[random.randint(0, len(stealthy_behaviour) - 1)])

    def low_attack(self):
        (self.name + " attacks low with a " + self.weapon)
    
    def high_attack(self):
        (self.name + " attacks high with a " + self.weapon)
    def throw_a_ninja_star(self):
        (self.name + " throws a ninja star.")
    
    
class Pirate:
    def __init__(self, name, weapon, rank, size):
        self.name = name
        self.weapon = weapon
        self.rank = rank
        self.size = size
    
    def __repr__(self) -> str:
        return "This pirate's name is " + self.name + " and they are armed with a " + self.weapon + ". They hold the rank of " + self.rank + '.'

    def say_pirate_stuff(self):
        pirate_stuff = ['Arrrr', 'Shiver me timbers!', 'Blow me down!', 'Yo ho ho and a bottle of rum!']
        print(self.name + " yells " + '"' + pirate_stuff[random.randint(0, len(pirate_stuff) - 1)] + '"')

    def low_attack(self):
        print(self.name + " attacks low with a " + self.weapon)
    
    def high_attack(self):
        print(self.name + " attacks high with a " + self.weapon)
    
    def fire_pistol(self):
        print(self.name + "fired a shot!")


ninja_one = Ninja('Hitori Hanzo', 'ninjato', 'ninja master', 'medium')

ninja_one.be_stealthy()
print(ninja_one.__repr__())

pirate_one = Pirate('Long John Silver', 'cutlass', 'pirate captain', 'medium')

pirate_one.say_pirate_stuff()
print(pirate_one.__repr__())



    