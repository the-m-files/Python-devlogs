#We are continuing what we were starting yesterday; which is nested if conditions
#these can be really helpful in some cases so here is an example:

brand = "Toyota"
year = "1935"

if brand == "Ford":
    if year == "1935":
        print("thats an old car")
    else:
        print("that is a good brand")
else:
    print("idk that brand")

#this is really simmilar to the and but is handy in certain cases such as games and stuff.
#but as you can see these two are practically identicle

if brand == "Ford" and year == "1935":
    print("that is a really old car")
elif brand == "Ford":
    print("good brand")
else:
    print("idk know that brand")

number = 2
print(3%2)
print(number%3 != 0 and number%4 != 0)

#--------------------------------------#
#        WHILE LOOPS STARTS HERE       #
#--------------------------------------#

#The while loop is a type of loop that will keep running until a certain condion is met.
x = 0
while x < 10:
    x += 1
    print(x)

#the while statment keeps running till 