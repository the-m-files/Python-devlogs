#mini project

class Character:

    game_name = "Journey of Ash"

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, amount):
        self.health -= amount
        print(f"took {amount} damage")

    #we need this because it tells python that the first arguments cls should be the class not the value we give it first
    @classmethod
    def change_game_name(cls, name):
        cls.game_name = name

    #this won't work because python automatically passes hero as attack if we try it. we need to add @staticmethod decorator
    @staticmethod
    def damage_calculator(attack, defense):
        if defense>attack:
            return 0
        else:
            return defense-attack
    
class Mage(Character):

    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self.mana=mana

    def take_damage(self, amount):
            self.health -= self.damage_after_shield(amount)
            print(f"took {self.damage_after_shield(amount)} damage")

    def cast_spell(self, cost):
        self.mana -= cost

    @staticmethod
    def damage_after_shield(damage):
        return damage/2
mage = Mage("gand", 100, 80)
mage.take_damage(40)
print(mage.health)
Mage.change_game_name("Realm of Ash")
print(mage.game_name)

print("-"*25)

class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"|N={self.name}, W={self.weight}, V={self.value}|"

    def __eq__(self, other):
        return True if self.value == other.value else False

    def __len__(self):
        return len(self.name)

class Weapon(Item):
    def __init__(self, name, weight, value, damage):
        super().__init__(name, weight, value)
        self.damage = damage
    def __str__(self):
        return f"{self.name.title()}--{self.damage}"

sword = Weapon("Iron Sword", 5, 100, 25)
potion = Item("Health Potion", 1, 30)

print(sword)
print(repr(sword))

print(potion)
print(repr(potion))

print(len(sword))

print(sword == potion)

#-----------------------------#
#           DUNDER            #
#-----------------------------#

#dunder methods as you can have seen above are quite useful. they can let you define how native methods interact with your class

#first off the bat we have __str__

#this one is fairly simple and here is how it is used:
#whenever python prints something it needs to be readable(str). So it would pass it through the __str__ method
#since we can define our own __str__ methods within our objects we can control what shows up when we use methods that need __str__ on our object

class example1:
    def __init__(self, name, species, age, color):
        self.name= name
        self.species = species
        self.age = age
        self.color = color

    def __str__(self):
        return self.name

#see how it returned user?
test1 = example1("user", "Homo sapien", 53, "Gray")
print(test1)

#after that we have __repr__, which is also similar to str but is mostly used for the devs for debugging and needs to be in a repr

class example2:
    def __init__(self, name, species, age, color):
        self.name= name
        self.species = species
        self.age = age
        self.color = color

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.name}, {self.species}, {self.age}, {self.color}"

test2 = example2("Cass", "Canine", 12, "Brown")
print(repr(test2))


#then we have __eq__ which stands to check if two objects are equal, notice i am not that advanced to handle different class objects
#to use it you need the "other" keyword meaning you have to have another object inside the method
class Food_item:
    def __init__(self, sugar, fats, calories):
        self.sugar = sugar
        self.fats = fats
        self.calories = calories

    def __eq__(self, other):
        if self.sugar+self.fats+self.calories==other.sugar+other.fats+other.calories:
            return True
        else:
            return False

#example:

chips = Food_item(3, 10, 350)
icecream = Food_item(10, 20, 200)

print(chips == icecream)

#And finally the len function, which is practilly the object telling what it should return for the user

class Tree:
    def __init__(self, height, name, color, region):
        self.height = height
        self.name = name
        self.color = color
        self.region = region

    def __len__(self):
        return self.height

#so when you ask for the len of tree it will return the tree's height.

Oak = Tree(16, "Oak", "Brown", "Plains")

print(len(Oak))

#and that is all of dunder man.