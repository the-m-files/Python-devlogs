#-----------------------------#
#             IN              #
#-----------------------------#

#the in keyword will check if something is a subset of some bigger subset

print("geo" in "geometry")

print("geoz" not in "Geometry")

#like that above this will work for dictionaries too

courses = {
    "Luch":["Chicken", "Beans", "Tortilla"],
    "Breakfast":["Cereal", "Panckakes", "Waffles"],
    "Dinner":["Soup", "Garlic Bread", "Pasta"]
}

print("Lunch" in courses)

#as you could have seen that this will also work

