#-----------------------------#
#           CLASSES           #
#-----------------------------#

#classes are the basic intro of Object Oriented Prgoramming. They work something like this:
#They are like blueprints and can be used and gave attributes to define unique properties


#here is a simple demonstration of me using class:

class fruit:

    taste = ""
    color = ""
    weight = None

#to actually use this we have to create an instance of an object refering to this class
#to do that it is pretty much like creating a variable:

#Object one; the Orange
Orange = fruit()
Orange.taste = "Sweet"
Orange.color = "Orange"
Orange.weight = 95

#Object two; the Pineapple
Papple = fruit()
Papple.taste = "Zesty"
Papple.color = "Yellow"
Papple.weight = 155

print(f"an orange has a {Orange.taste} taste it has a {Orange.color} color and weighs about {Orange.weight} grams")
print(f"a Pineapple has a {Papple.taste} taste it has a {Papple.color} color and weighs about {Papple.weight} grams")

#notice, you can also acess these terms seperately:

print(Orange.color, Orange.taste, Papple.weight)

#-----------------------------#
#           METHODS           #
#-----------------------------#

#Methods are litterally adding def functions inside classes in python. They are pretty easy to understand and called

class classroom():
    width = 0
    height = 0
    def calcarea(self):
        return self.height*self.height

#this is an instance of creating and using methods. Don't worry about the self keyword
class1 = classroom()
class1.width = 100
class1.height = 100
print(class1.calcarea())

