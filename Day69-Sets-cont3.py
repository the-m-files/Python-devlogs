#-----------------------------#
#          FROZENSET          #
#-----------------------------#

#a frozen set is an immutable set meaning it can't be edited in any way and can be used as a dict key
#the only way to create one is using the frozenset() method.

planets = frozenset(["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"])

#this will raise an error:
#planets.remove("mercury")

#but methods like issuperset will continue to work.
print(planets.issuperset({"mercury", "earth"}))
