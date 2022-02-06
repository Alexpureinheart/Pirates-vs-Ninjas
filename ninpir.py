import random

ninja_names = ['Fujibayashi Nagato', 'Momochi Sandayu', 'Ishikawa Goemon', 'Hattori Hanzo', 'Mochizuki Chiyome', 'Fuma Kotaro', 'Jinichi Kawakami',
'Joe Musashi', 'Ryu Hayabusa', 'Stephen Hayes']

pirate_names = ['Long John Silver', 'Redbeard', 'Blackbeard', 'Francis Drake', 'Samuel Bellamy', 'Ching Shih',
'Bartholomew Roberts', 'Captain Kidd', 'Henry Morgan', 'Calico Jack']

pirate_weapons = ['cutlass', 'saber', 'dagger', 'axe']
ninja_weapons = ['ninjato', 'katana', 'yari', 'tanto']

pirate_ranks = ['pirate captain', 'legend of the seas', 'dread pirate', 'scourge of the seven seas']
ninja_ranks = ['ninja master', 'mystical ninja', 'ninja sensei', 'ninja assassin']

sizes = ['small', 'medium', 'large']


class Ninja:
    def __init__(self, name, weapon, rank, size):
        self.name = name
        self.weapon = weapon
        self.rank = rank
        self.size = size
        engaged_in_battle = False 
        is_dead = False 
        health_points = 10
    
    def __repr__(self) -> str:
        return self.name
    
    def be_stealthy(self):
        stealthy_behaviour = ['creeping around.', 'purching up high.', 'hiding in the water.', 'pretending to be a monk.']
        print(self.name + " is " + stealthy_behaviour[random.randint(0, len(stealthy_behaviour) - 1)])

    def low_attack(self, opponent):
        print(self.name + " attacks " + opponent + " low with a " + self.weapon + "!")

    def high_attack(self, opponent):
            print(self.name + " attacks " +  opponent + " high with a " + self.weapon + "!")

    def throw_a_ninja_star(self, opponent):
            print(self.name + " throws a ninja star at " + opponent + "!")

    def low_block(self, opponent):
            print(self.name + " blocks " + opponent + " low with their " + self.weapon + "!")

    def high_block(self, opponent):  
            print(self.name + " blocks " + opponent + " high with their " + self.weapon + "!")

    

    
    
class Pirate:
    def __init__(self, name, weapon, rank, size):
        self.name = name
        self.weapon = weapon
        self.rank = rank
        self.size = size
        is_dead = False
        engaged_in_battle = False
        health_points = 10
    
    def __repr__(self) -> str:
        return self.name

    def say_pirate_stuff(self):
        pirate_stuff = ['Arrrr', 'Shiver me timbers!', 'Blow me down!', 'Yo ho ho and a bottle of rum!']
        print(self.name + " yells " + '"' + pirate_stuff[random.randint(0, len(pirate_stuff) - 1)] + '"')

    def low_attack(self, opponent):
            print(self.name + " attacks " + opponent + " low with a " + self.weapon + "!")
    
    def high_attack(self, opponent):
            print(self.name + " attacks " +  opponent + " high with a " + self.weapon + "!")
    
    def fire_pistol(self, opponent):
            print(self.name + "fired a shot at " + opponent + "!")
        
    def low_block(self, opponent):
            print(self.name + " blocks " + opponent + " low with their " + self.weapon + "!")
    
    def high_block(self, opponent): 
            print(self.name + " blocks " + opponent + " high with their " + self.weapon + "!")
    

def random_picker(list):
    return list[random.randint(0, len(list) - 1)]

def ninja_generator(name):
    return Ninja(name, random_picker(ninja_weapons), random_picker(ninja_ranks), random_picker(sizes))

def pirate_generator(name):
    return Pirate(name, random_picker(pirate_weapons), random_picker(pirate_ranks), random_picker(sizes))

pirate_one = pirate_generator(random_picker(pirate_names))
ninja_one = ninja_generator(random_picker(ninja_names))


pirate_one.high_attack(ninja_one.name)
ninja_one.high_block(pirate_one.name)
ninja_one.low_attack(pirate_one.name)
pirate_one.low_block(ninja_one.name)
pirate_one.fire_pistol(ninja_one.name)
ninja_one.throw_a_ninja_star(pirate_one.name)
ninja_one.be_stealthy()
pirate_one.say_pirate_stuff()








