#-----------------------------#
#       INVENTORY / ITEMS     #
#-----------------------------#

class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.inventory = []

    def add(self, item):
        self.inventory.append(item)

    def display_inventory(self):
        display_dict = {}

        for item in self.inventory:
            if item.name not in display_dict:
                display_dict[item.name] = 0

            display_dict[item.name] += 1

        for name, quantity in display_dict.items():
            print(f"{name} × {quantity}")

    def view_stats(self):
        x = 8
        print(f'{"=" * x}| {self.name.capitalize()} |{"=" * x}')
        print(f'{" " * int(x / 2)}health: {self.health}')
        print()
        print(f'{"=" * x}| Inventory |{"=" * x}')
        self.display_inventory()

    def use_item(self, item):
        if item in self.inventory:
            item.use_item(self)

            if item.consumable:
                self.inventory.remove(item)


class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value
        self.consumable = None


class Weapon(Item):
    def __init__(self, name, weight, value, damage):
        super().__init__(name, weight, value)
        self.damage = damage
        self.consumable = False

    def use_item(self):
        print(f"{self.name} attacked")


class Potion(Item):
    def __init__(self, name, weight, value, heal_amount):
        super().__init__(name, weight, value)
        self.heal_amount = heal_amount
        self.consumable = True

    def use_item(self, user):
        user.health += self.heal_amount
        print(f"{self.name.capitalize()} restored {self.heal_amount} HP")


class Shield(Item):
    def __init__(self, name, weight, value, defense):
        super().__init__(name, weight, value)
        self.defense = defense
        self.consumable = False

    def use_item(self):
        print(f"{self.name} was equipped")


# Objects

sword = Weapon("Iron Sword", 8, 30, 50)
potion = Potion("Health Potion", 1, 15, 30)
shield = Shield("Wooden Shield", 8, 35, 10)

cooldude = Character("cool_kid", 100)

cooldude.add(potion)
cooldude.add(potion)
cooldude.add(sword)
cooldude.add(sword)
cooldude.add(shield)

cooldude.view_stats()

cooldude.use_item(potion)

print(cooldude.health)

cooldude.display_inventory()