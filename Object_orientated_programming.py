import random
Goblins = ["Blurk", "Floow", "Wrumpf", "Brubblu", "Trully", "Blark", 'ax','tiokx', 'ez', 'glilb''lierk', 'prusakz', 'aaleld', 'kleezmuics', 'xirgieng','kibsoix']

class goblin:
    "Attributes"
    def __init__(self):
        self.name = random.choice(Goblins)
        self.strength = random.randint(60, 70)
        self.hitpoints = random.randint(100, 130)
    #"methods"
    def show_stats(self):
        print(self.name)
        #f string format for combinig variables with strings.
        print(f"strength {self.hitpoints}")
        print(f"hitpoints {self.strength}")
    def attack(self):
         damage = self.strength + random.randint(10, 30)
         print(f"damage {damage}")
         return damage
class FireGoblin(goblin):
    def __init__(self):
        super().__init__()
        self.name = "Fire " + self.name
    def attack(self):
        damage = random.randint(self.strength-20, self.strength)
        print(self.name, "throws a FIREBALL!")
        return damage    
class player:
    def __init__(self):
            self.name = "Frans"
            self.strength = 150
            self.hitpoints = 200
            self.weapon = "gnarly stick"
            self.armor = "bedsheet"
    def show_stats(self):
            print(self.name)
            #f string format for combinig variables with strings.
            print(f"strength {self.strength}")
            print(f"hitpoints {self.hitpoints}")
    def wound(self,damage):
        player1.hitpoints-=(damage)
        print(player1.hitpoints)

def fight(player1, goblin1):
     while player1.hitpoints >0  and goblin1.hitpoints >0:
        damage = goblin1.attack()
        player1.wound(damage)

goblin1 = FireGoblin()
goblin1.show_stats()
player1= player()
player1.show_stats()
fight(player1, goblin1)


