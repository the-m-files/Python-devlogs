#-----------------------------#
#          ISINSTANCE         #
#-----------------------------#

#isinstance is fairly simple to understand and use, it is used to check if an object is a given class:
#this is the common anatomy of the function:

#isinstance(object, classinfo)

#object is the var/value you want to check

#int/str/tuple/other

# Checking native data types
isinstance(5, int)          # Returns True
isinstance("Hello", list)   # Returns False

# Checking against multiple types
isinstance(3.14, (int, float)) # Returns True

#-----------------------------#
#           CLASSES           #
#-----------------------------#

#creating a class:

class pet:
    def __init__(self, animal, species):
        self.animal = animal
        self.species = species


dog = pet("Dog", "Canis Lupis")

print(dog)

print(dog.species)
print(dog.animal)

