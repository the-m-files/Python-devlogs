#-----------------------------#
#         CONSTRUCTORS        #
#-----------------------------#

#A constructor is a special method that automatically runs whenever an object
#is created from a class.

#In Python, the constructor is named __init__().

class Dog:

    #This constructor runs automatically when a Dog object is created.
    def __init__(self, name, age):
        self.name = name      #Store the dog's name
        self.age = age        #Store the dog's age

    def bark(self):
        print(f"{self.name} says Woof!")

#Create two Dog objects.
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

#Access the attributes that were created by the constructor.
print(dog1.name)
print(dog2.age)

#Call a method.
dog1.bark()
dog2.bark()

"""
OUTPUT
------
Buddy
5
Buddy says Woof!
Max says Woof!
"""

#-----------------------------#
#        IMPORTANT NOTES      #
#-----------------------------#

#1. __init__() is called automatically.
#2. It initializes (sets up) the object's starting data.
#3. self refers to the current object.
#4. Every object gets its own copy of the attributes.
#5. __init__() does NOT create the object—it only prepares it.

#-----------------------------#
#         INHERITANCE         #
#-----------------------------#

#inheritance is a concept that makes it so that you can make sub classes of classes. these subclasses will inherit 
#their parent classes functions(modules) and blueprints plus whatever you add in the subclass

#Here is a class

class vehical():
    size = ""
    def saycolor(self):
        print(self.size, "is a good size")

#this is a subclass meaning it will inherit the size attribute and saycolor module
class car(vehical):
    color = ""
    horsepower = 0
    def review(self):
        print(self.horsepower, "horsepower and ", self.color, "is a good combo but the size of", self.size, "might be good or bad")

toyota = car()
toyota.color = "white"
toyota.horsepower = 70
toyota.size = 9
toyota.review()
toyota.saycolor()

#-----------------------------#
#       MODULE OVERIDING      #
#-----------------------------#

#you know how in css if you write it inline it will ignore the one you wrote in the folder? the closer you get to the object 
#the higher ones get ignored? that is the same deal here.


class Animal:

    # attributes and method of the parent class
    name = ""
    
    def eat(self):
        print("I can eat")

# inherit from Animal
class Dog(Animal):

    # override eat() method
    def eat(self):
        print("I like to eat bones")

# create an object of the subclass
labrador = Dog()

# call the eat() method on the labrador object
labrador.eat()

#-----------------------------#
#            SUPER            #
#-----------------------------#

#In the last concept from inheritance, we learned that a subclass can override
#a method from its parent class.

#If we still want to use the parent's version of that method, we can use
#the super() function.

class parent():

    def parentmethod(self):
        print("This is the parent method.")

class child(parent):

    def parentmethod(self):
        print("I am the child method.")

        #Call the parent's version of parentmethod().
        super().parentmethod()

kid = child()

kid.parentmethod()

"""
OUTPUT
------
I am the child method.
This is the parent method.
"""

#-----------------------------#
#      USING SUPER WITH       #
#       CONSTRUCTORS          #
#-----------------------------#

#super() is most commonly used with constructors (__init__()).

class Animal():

    def __init__(self, name):
        self.name = name
        print("Animal constructor ran.")

class Dog(Animal):

    def __init__(self, name, age):

        #Run the parent's constructor first.
        super().__init__(name)

        #Now add attributes specific to Dog.
        self.age = age

dog = Dog("Buddy", 3)

print(dog.name)
print(dog.age)

"""
OUTPUT
------
Animal constructor ran.
Buddy
3
"""

#-----------------------------#
#        IMPORTANT NOTES      #
#-----------------------------#

#1. super() gives you access to the parent class.
#2. It is commonly used to call methods from the parent.
#3. The most common use of super() is calling the parent's constructor.
#4. super().__init__() prevents you from rewriting the parent's initialization
#   code in every subclass.
#5. It helps keep your code clean and avoids duplication.