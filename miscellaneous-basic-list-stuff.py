#lists
#lists are the most basic and begginer friendliest type of iterable, 

#to make a list here is how you define it:

mylist = [1, 2, 3, 4, 5, 6] #a list can have multiple same characters and be any legnth long and can be dynamically updated. 

#to get the n-th item of a list, you can use the basic syntax like this:

print(mylist[0]) #lists start counting from 0.

#to add something to your list you can use the append method. 

mylist.append(7) #append basically adds whatever value you give it to the end of the list.
#to be honost lists can contain anything:

random = [2, "banana", "monkey", 42, True, False, 0, [31, 23 , 4]] #yeah, lists can contain other lists too. and other datatypes. 

#to replace something in a list we can also use a similar syntax like this:
mylist[3] = "this position has been replaced" 
print(mylist[3])

#to merge two different lists, we can simply use the add operator
print(mylist+random)

#to insert an element in a specific position we can use the insert property

mylist.insert(2, "this was inserted at line 28")


  
