#-----------------------------#
#         INHERITANCE         #
#-----------------------------#

#I know we have went over this in day 52-53. This is were i truly understand it.
#inheritance is a python concept where we can make it so that some classes "inherit" the methods of other classes and attributes

#here is an example:

class dog:

    def __init__(self, name, age):
        self.name=name
        self.age=age

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class cat:

    def __init__(self, name, age):
        self.name=name
        self.age=age

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

maxy = dog("max", 5)
bosko = cat("bosko", 2)
bosko.sleep()
maxy.eat()
maxy.sleep()

print("-"*25)

#notice how the code is repetative? like how both of these are the same? we can use inheritance to our advantage here

#first we create a parent class that is going to share similar methods.
class animal:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class dog1(animal):
    pass

class cat1(animal):
    pass


#notice how we create(re-assign) objects yet even though the classes are nothing the parent takes care of it.
#the child classes don't have anything in them. they use the parent calsses code and this is way more efficient
maxy = dog1("max", 5)
bosko = cat1("bosko", 2)
bosko.sleep()
maxy.eat()
maxy.sleep()

#but you may ask why use seperate classes? why can't we just use the animal? is this just for aesthetic?
#well. No... You can do much more such as adding unique methods for sub classes as done bellow:

class dog1(animal):

    def bark(self):
        print(f"{self.name} barks at you")

class cat1(animal):

    def meow(self):
        print(f"{(self.name).capitalize()} meows at you")

    
maxy = dog1("max", 5)
bosko = cat1("bosko", 2)
maxy.bark()
bosko.meow()

#Here is a new fully working demo on this topic bellow:

class vehical():
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def drive(self):
        print("you are driving")

class Bike(vehical):
    def ring_bell(self):
        print("you ring the bell")

class Car(vehical):
    def honk(self):
        print("you are honking")

car = Car("Toyota", 80)
bike = Bike("Trek", 20)

car.drive()
car.honk()

bike.drive()
bike.ring_bell()

#-----------------------------#
#         COMPOSITION         #
#-----------------------------#

#THIS IS SO HARD TO GRASP MIGHT RE-WRITE NOTES LATER.
#anyways. here is what i understand: composition is the act of putting objects inside of objects. they are kind of complex to grasp

#here is a small example of what i understand:

class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

class Tires:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, brand, horse_power, size):
        self.brand = brand
        self.engine = Engine(horse_power)
        self.tire = Tires(size)

    def display(self):
        print(f"{self.brand} {self.engine.horse_power}(hp) {self.tire.size}in")

car1 = Car("checkor", 250, 16)
car1.display()

car2 = Car("ford", 300, 17.5)
car2.display()

#this is my understanding of how this works:

#self.engine.horse_power
#self --> go to the object that called this
#engine --> in the object that we are in go to the part that object inside of it that says engine
#horse_power --> once in engine we can go ahead and check the value of the horse_power attribute