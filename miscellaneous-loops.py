#the first type of loops are iterables, lets see how they work
#lets use a string to keep things easy

name = input("enter your name to check how many letter 'a' there are: ")
a_in_name = 0
for letter in name:
  if letter == "a" or letter == "A":
    a_in_name +=1
print(a_in_name)

#there is an easier method called "count()" but obviosly my students didn't know it

print(name.count("a"))

#coming back to the loops again, here is an example with a list:

grades = [100, 78, 89, 94, 99, 65, 90, 80, 55]

for grade in grades:
  if grade < 55:
    print("Failure")
  else:
    print("Passes")


#and finally here is the one with range:

for i in range(0, 10):
  if i%2==0:
    print(i, "is even")


