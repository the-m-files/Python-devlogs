#-----------------------------#
#      MULTI INHERITANCE      #
#-----------------------------#

#Like how we can make child classes from parent classes we can also make child classes from multiple parents
#for example it is like how a shark is a mammal but also a sea creature

class parent1():
    def hello(self):
        print("hello")

class parent2():
    def hi(self):
        print("hi")

class child1(parent1, parent2):
    pass

#-----------------------------#
#      OOP REVIEW (PART 1)    #
#-----------------------------#

#Today I learned about three important OOP concepts:
#1. self
#2. __init__()
#3. super()

#-----------------------------#
#             SELF            #
#-----------------------------#

#self refers to the current object.
#Every object has its own copy of its attributes.

class Dog:

    def __init__(self, name):
        self.name = name

dog1 = Dog("Buddy")
dog2 = Dog("Max")

print(dog1.name)
print(dog2.name)

"""
OUTPUT
------
Buddy
Max
"""

#-----------------------------#
#          __INIT__           #
#-----------------------------#

#__init__() is a special method (constructor).
#It automatically runs whenever a new object is created.
#Its job is to initialize (set up) the object's starting attributes.

class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

cat = Animal("Whiskers", 2)

print(cat.name)
print(cat.age)

"""
OUTPUT
------
Whiskers
2
"""

#-----------------------------#
#           SUPER()           #
#-----------------------------#

#super() allows a child class to use code from its parent class.
#The most common use is calling the parent's constructor so we don't
#have to rewrite the code that initializes shared attributes.

class Parent:

    def __init__(self):
        print("Parent constructor ran.")

class Child(Parent):

    def __init__(self):
        super().__init__()
        print("Child constructor ran.")

child = Child()

"""
OUTPUT
------
Parent constructor ran.
Child constructor ran.
"""

#-----------------------------#
#        IMPORTANT NOTES      #
#-----------------------------#

#self        -> Refers to the current object.
#__init__()  -> Runs automatically when an object is created.
#super()     -> Calls code from the parent class.
#
#Think of it this way:
#
#Parent: "I'll set up everything every animal needs."
#Child:  "I'll let the parent do that first, then I'll add my own stuff."
#
#Attributes = Data (name, age, breed)
#Methods    = Actions (bark, meow, introduce)