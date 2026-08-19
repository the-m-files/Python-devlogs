#------------------------------#
#           FOR LOOP           #
#------------------------------#

#the for loop is used to iterate some stuff and maybe used as a loop to iterate over stuff

food = "Maple syrup and Pancakes"

for c in food:
    print(c)

#c could be any value you want, it can also be multiple letters
#c is set to a single letter of "food" and when we print c we can see it
#this will keep running until all letters of food are scanned.

fruits = ["Apple", "Banana", "Strawberry", "Kiwi", "Grape"]

for fruit in fruits:
    print(fruit)

def addlis(lis):
    total = 1
    for number in lis:
        
        total = number*total
    return total

print(addlis([3,2]))

numberslist = [1,2,3,4,5,6,7,8,9]
total1 = 0
for number in numberslist:
    if number%2 == 0:
        total1 = number+total1
    else:
        number = total1

print(total1)

def concatenate(listt):
    total2 = ""
    for L in listt:
        if len(L)>2:
            total2 = total2+L
        

    return total2
print(concatenate(["ac", "dei", "fgh", "ich"]))

#REVERSED STARTS HERE

games = ["soccer", "volleyball", "chess", "football", "basketball"]
print(reversed(numberslist))
print(type(reversed(numberslist)))

#this for loop will print out the reversed items in games
for i in games[::-1]:
    print(i)
print("-"*25)
#this is almost the same thing:
for i in reversed(games):
    print(i)

#notice this will only work once. you have to generate a new one every time.