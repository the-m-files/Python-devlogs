class Student():
    def __init__(self, name, grade, fav_subject):
        self.name = name
        self.grade = grade
        self.fav_subject = fav_subject
    def introduce(self):
        print(f"{self.name} is my name and i am in grade {self.grade}")

    def study(self):
        print(f"{self.name} is studying {self.fav_subject}, {self.name} graduated grade {self.grade}")
        self.grade += 1
        print(f"{self.name} is now in grade {self.grade}")
        
Ian = Student("Ian", 1, "Science")
Ian.introduce()
Ian.study()
print("-"*25)

#-----------------------------#
#     MODIFYING ATTRIBUTES    #
#-----------------------------#

#it is possibly to change the value of attributes over time here is how they are used:

class Human:
    def __init__(self, name, age, fav_food):
        self.name = name
        self.age = age
        self.fav_food = fav_food

    def introduce(self):
        print(f"Hi, I am {self.name}. I am {self.age} years old, and my favorite food is {self.fav_food}")

    def happybday(self):
        print(f"happy birthday to me! I am now {self.age+1} years old")
        self.age +=1

    def eat(self):
        print(f"I am eating {self.fav_food} now. Can't talk")

    def talk(self):
        urname = str(input("Whats your name? "))
        print(f"nice to meet you {urname}!")
        print(f"i like to eat {self.fav_food}")
        print('it was good meeting you')


dude1 = Human("Gary", 10, "Pies")
dude1.talk()
print("-"*25)

#notice how in happybday method we are changeing self.name +=1. it actually saves. that is pretty much it


#-----------------------------#
#   METHODS WITH PARAMETERS   #
#-----------------------------#

#in methods we can include parameters to do stuff from our point of view

class BankAccount:

    def __init__(self, balance, owner):
        self.balance = balance
        self.owner = owner

    def withdraw(self, amount):
        if self.balance < amount:
            print("not enough money")
        else:
            self.balance -= amount
            print(f"your current balance is {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"your current balance is {self.balance}")

    def change_owner(self, newowner):
        self.owner = newowner
        print(f"the current owner is {self.owner}")


Hue = BankAccount(0, "Hue")

Hue.deposit(100)
Hue.withdraw(17)
Hue.change_owner("Gary")
