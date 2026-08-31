#-----------------------------#
#         ENCAPSULATION       #
#-----------------------------#

#encapsulation means limiting how data is handled in your function and the rest of the code.
#so other parts just don't mess with the inner variables of your class

#we can accomplish this by two ways, using getter and setter methods.
#these do not mean anything, but are just terms that represent the purpose of a function that is used for encapsulation

#here is how to set a getter method which limits people on how much/what data they can retrieve from a class

class  Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

vj = Character("VJ", 100)

#notice how people can just change it outside the function? and if you have any if conditions saying it can't be lower than zero,
#well, now it is.
vj.health -= 110

#to prevent this we can define only a getter method without the setter made so it will raise an error
#becuase we defined how to "read" a variable but not how to "write" it.

class  Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    @property    #this is the property method, we are defining the property of health across our code. aka a getter
    def health(self):
        return self.health

    @health.setter   #and this is the setter, which is constraining our program to keep health above 0
    def health(self, value):   
        if value < 0:
            self._health = 0
        else:
            self._health = value

class Character:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    @property
    def health(self):
        return f"{self.name}: {self._health}"

    @health.setter
    def health(self, amount):
        if amount>100:
            self._health = 100
        elif amount<0:
            self._health = 0
        else:
            self._health = amount

Mage = Character("Gander", 100)
Mage.health = 119
print(Mage.health)
Mage.health = -10
print(Mage.health)

#-----------------------------#
#         POLYMORPHISM        #
#-----------------------------#

#this is pretty simple. all there is to this concept are that you don't need to know what an ibject is before acting up on it
#meaning the same thing can have multiple forms

class Char:                             #one parent class
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self):
        print("Char attacked")

#and multple child classes that all have the same stuff as parent but just a small difference in their methods:
class Warrior(Char):
    def __init__(self, name, health):
        super().__init__(name, health)

    def attack(self):
        print(f"{self.name} swung sword")

class Mage(Char):
    def __init__(self, name, health):
        super().__init__(name, health)

    def attack(self):
        print(f"{self.name} casts spell")

class Archer(Char):
    def __init__(self, name, health):
        super().__init__(name, health)

    def attack(self):
        print(f"{self.name} fires arrow")

class Healer(Char):
    def __init__(self, name, health):
        super().__init__(name, health)

    def attack(self):
        print(f"{self.name} Heals all")

def start_battle(characters):
    for character in characters:
        character.attack() #notice how character is one variable but is behaving differently for each iteration?
                            #that is polymorphism for short

G1 = Warrior("Knight", 100)
G2 = Mage("Gandalf", 100)
G3 = Archer("Robin", 100)
G4 = Healer("Priest", 100)

characters = [
    G1,
    G2,
    G3,
    G4
]

start_battle(characters)