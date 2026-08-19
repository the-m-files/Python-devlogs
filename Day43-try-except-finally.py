#-----------------------------#
#     TRY, EXCEPT, FINALLY    #
#-----------------------------#

#try will tell python to test what first, ecxept will tell an exception if it sees an error and finally will give it an awnser

#this code bellow is fragile, the user can type 0 or anything not a number and will return an error

#number = int(input("type a number "))
#print(1/number)

#to fix this we can use these keywords above:

try:
    number = int(input("type a number"))
    print(1/number)
except ValueError:
    print("give another number")
except ZeroDivisionError:
    print("you cant use zero")

#-----------------------------#
#      DYNAMIC VAR NAMES      #
#-----------------------------#

#to ever change a variable/create a variable while running the python program, you can use three methods:

#method one:
# Create an empty dictionary to hold your "variables"
user_data = {}

# Ask the user for the "variable name" and its value
variable_name = input("Enter a key name (e.g., 'age'): ")
variable_value = input("Enter the value for this key: ")

# Store it in the dictionary
user_data[variable_name] = variable_value

# Access the data safely
print(user_data)
print(f"The value of {variable_name} is {user_data[variable_name]}")


#method two:
# Dynamically naming a variable based on user input
dynamic_name = input("Enter your variable name: ")  # User types: player_score

# Create the global variable name and assign it a value
globals()[dynamic_name] = 100

#NOTICE THIS IS HIGHLY RISKY. YOU NEED TO KNOW WHAT THEY WILL TYPE BEFORE HAND
# You can now call it directly in your code if you know what the user typed
print(player_score)  # Outputs: 100

