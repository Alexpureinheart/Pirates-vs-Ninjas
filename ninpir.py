import random

class Ninja:
    def __init__(self, name, weapon, rank, size):
        self.name = name
        self.weapon = weapon
        self.rank = rank
        self.size = size
    
    def be_stealthy(self):
        stealth_behaviour = ['creeping around.', 'purching up high.', 'hiding in the water.', 'pretending to be a monk.']


    def low_attack(self):
        (self.name + " attacks low!")
    
    def high_attack(self):
        (self.name + " attacks high!")

    
    
class Pirate:
    def __init__(self, name, weapon, rank, size):
        self.name = name
        self.weapon = weapon
        self.rank = rank
        self.size = size

    def say_pirate_stuff(self):
        pirate_stuff = ['Arrrr', 'Shiver me timbers!', 'Blow me down!', 'Yo ho ho and a bottle of rum!']
        print(self.name + " yells: " + pirate_stuff[random.randint(0, len(pirate_stuff) - 1)])

    def low_attack(self):
        print(self.name + " attacks low!")
    
    def high_attack(self):
        print(self.name + " attacks high!")
    
    def fire_pistol(self):
        print(self.name + "fired a shot!")



    