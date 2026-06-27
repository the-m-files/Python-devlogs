#Lets start from where we left off. the else statement we will just have a minor revision
#The else statment will run if the first "if" parametr is false. It won't run when it is true
if "500" == "500":
    print("this is correct!")
else:
    print("this is imposssible")

if "500 " == "500":
    print("this is correct!")
else:
    print("this is will run because of the space")

#--------------------------------------#
#      ELIF STATEMENT STARTS HERE      #
#--------------------------------------#

#the elif statment is like the else statment but can be stacked. 
#for example if you know there can only be four items you can buy you will eveuntually find the cheapest by checking everything
#we can use the elif statment for that because it will run whenever the elif/if statment is false above it.
money = 30
budget = 25  # Changed budget to 25 so earlier conditions are false
apple = 5
banana = 7
mango = 4
cherry = 1

if money - apple < budget: 
    print("you can buy the apple")
elif money - banana < budget: 
    print("you can buy the banana")
elif money - mango < budget: 
    print("you can buy the mango")  # This will trigger!
elif money - cherry < budget: 
    print("you can buy the cherry")

print(abs(3))

#--------------------------------------#
#     TERNARY STATEMENT STARTS HERE    #
#--------------------------------------#

#Ternary is a simple way of writing an if else block in one line. it exists in js.
#Example: this one function checks wether a number is negative

def negorpos(number):
    number = "Positve" if number > 0 else "Negative"
    return number

print(negorpos(-4))
print(negorpos(4))

#WARNING: ADDING AN ELIF WILL NOT WORK
#here is its anatomy:
# number(1) = "Positve"(2) if(3) number < 0(3a) else(4) "Negative"(4a)
#
#1) this is the variable where the result is stored
#2) the string "Postive" is the result the var number will get when the if condion becomes true
#3) the if condition determines whether the variable will store the string "Postive" through the condtions 3a
#3a) this is the condtions that determines if number gets the value "Positve" by checking if a number is positive
#4) this is the fallback operator that will take care of any other values. it will automatically assign number the string negative
#4a) this is the value give so that the else will assign the this to number

#--------------------------------------#
#       AND STATEMENT STARTS HERE      #
#--------------------------------------#

#The and function starts here it is what it says and will let you check if two conditions are true at the same instance.

if 5>7 and "rain" == "rain":
    print("yes this wont work")

if 5<7 and "rain" == "rain":
    print("yes this works")

if 5<7 and 3<6 and 1<4 and "rain" == "rain":
    print("You can stack multiple ands to get as much condtions to be right at the same time")

#--------------------------------------#
#        OR KEYWORD STARTS HERE        #
#--------------------------------------#

#The or keyword is similar of to that of the and keyword. unlike the and function it will say it is true even if one of the
#conditions to be true

if "name" == "name" or 6==3:
    print("the or function will let this slide")

if  4+3 == 3 or 6==3 or "name" == "name":
    print("like the and it can also stack")

if   6==3 or "name" == "name":
    print("Oh, also the order of the condions won't matter")

#--------------------------------------#
#        NOT KEYWORD STARTS HERE       #
#--------------------------------------#

#The not key word is something that will reverse/inverse the return value of a condtion
#for example it is the ! for !=

print(not True)
print(not False)

if "x" in "Hello":
    print("this will not print")

if "x" not in "Hello":
    print("since i added the not in the conditons")

value = 10

if value > 100:
    print("this will work")

if value < 100:
    print("this will not work")
    
if not value > 100:
    print("this will work")

print("Python" if 5> 0 and 6> 0 else "Yikes")