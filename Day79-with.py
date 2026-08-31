# ------------------------------------------ #
#       CONTEXT MANAGERS & THE "with"       #
# ------------------------------------------ #

# A context manager lets us automatically run
# setup code before something happens and cleanup
# code afterward.

# The most common example is opening a file:

with open("test.txt", "w") as file:
    file.write("Hello!")

# The file is automatically closed when the
# "with" block finishes.


# ------------------------------------------ #
#              __enter__()                  #
#              __exit__()                   #
# ------------------------------------------ #

# Context managers use two special methods:
#
# __enter__() -> runs when entering the "with"
# __exit__()  -> runs when leaving the "with"


class Test:

    def __enter__(self):
        print("Starting!")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Ending!")


with Test():
    print("Inside!")


# Output:
#
# Starting!
# Inside!
# Ending!


# ------------------------------------------ #
#                    as                     #
# ------------------------------------------ #

# __enter__() can return a value.
# We can store that value using "as".


class Greeting:

    def __enter__(self):
        return "Hello!"

    def __exit__(self, exc_type, exc_value, traceback):
        print("Goodbye!")


with Greeting() as message:
    print(message)


# Output:
#
# Hello!
# Goodbye!


# ------------------------------------------ #
#              HOW IT WORKS                 #
# ------------------------------------------ #

# When Python sees:

with Test():
    print("Hello")


# It roughly follows this idea:
#
# 1. Call __enter__()
# 2. Run the code inside the with block
# 3. Call __exit__()


# ------------------------------------------ #
#              WHY USE IT?                  #
# ------------------------------------------ #

# Context managers are useful when something
# needs to be:
#
# 1. Set up
# 2. Used
# 3. Cleaned up
#
# Examples:
#
# - Opening files
# - Database connections
# - Locks
# - Temporary resources
#
# The "with" statement makes cleanup happen
# automatically.


# ------------------------------------------ #
#               TODAY'S IDEA                #
# ------------------------------------------ #

# A context manager controls what happens
# BEFORE and AFTER a block of code.
#
# __enter__() -> before
# __exit__()  -> after
#
# with something:
#     code
#
# is the basic syntax.


# ------------------------------------------ #
#                CHALLENGE                  #
# ------------------------------------------ #

# Make a Timer context manager.
#
# It should:
#
# 1. Print "Starting..." when entering
# 2. Record the current time
# 3. Run the code inside the with block
# 4. Print "Finished!" when leaving
# 5. Print how many seconds the code took
#
# Example:
#
# with Timer():
#     time.sleep(2)
#
# Expected:
#
# Starting...
# Finished!
# Time: 2.00 seconds