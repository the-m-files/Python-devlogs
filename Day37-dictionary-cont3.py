#-----------------------------#
#         MODIFICATION        #
#-----------------------------#

#to add/replace a key value pare you can use something similar to a list syntax ways


courses = {
    "Luch":["Chicken", "Beans", "Tortilla"],
    "Breakfast":["Cereal", "Panckakes", "Waffles"],
    "Dinner":["Soup", "Garlic Bread", "Pasta"]
}


#notice how it doesn't give a value eror?
courses["Dessert"] = ["ice cream", "Cheese cake", "Chocolate"]

print(courses["Dessert"])

print(courses)

#notice you can also you use the dict() keyword

bank = {
    "debit":"$3.74",
    "credit":"-900"
}

#you can also use this:
#order = dict()

print(bank)

bank["credit"] = "-935"

print(bank)
print("-"*25)
#notice how you can add/change key value pairs

#-----------------------------#
#          SET DEFUALT        #
#-----------------------------#

#this is a method that will add a key value pair when it cannot find one in the dictionary. It will add it to the dictionary on the fly


shapes = {
    "square":4, 
    "rectangle":4, 
    "circle":0,
    "pentagon":5,
}

print(shapes.get("triangle", 3))

#so as you can see this has returned the value 3 when it found out that triangle didn't exists in the shapes dicrionary
#but this has one problem tho, it will need to written again and again everytime you use it. To fix it we can use the set defalut

shapes.setdefault("triangle", 3)

print(shapes)

#notice how it is added when we print the list again?



