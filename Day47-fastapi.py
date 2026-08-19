#-----------------------------#
#       FASTAPI DEVLOG        #
#-----------------------------#

# FastAPI is a Python framework used to build web APIs.
#
# An API allows different programs to communicate with each other.
#
# We will build a small API and use FastAPI's automatic
# documentation to interact with it.
#
# First, install FastAPI and Uvicorn:
#
# pip install fastapi uvicorn
#
# Then run this file with:
#
# uvicorn main:app --reload
#
# After that, go to:
#
# http://127.0.0.1:8000/docs
#
# This will open FastAPI's interactive documentation.
# You can click "Try it out" and "Execute" to test
# each endpoint.


from fastapi import FastAPI


#-----------------------------#
#       CREATING THE APP      #
#-----------------------------#

# This creates our FastAPI application.
#
# "app" represents our API.
#
# We will use "app" to create endpoints (routes)
# that users and other programs can interact with.

app = FastAPI()


#-----------------------------#
#          FIRST ROUTE        #
#-----------------------------#

# This is a DECORATOR.
#
# @app.get("/hello") tells FastAPI:
#
# "When someone sends a GET request to /hello,
#  run the function directly below."
#
# GET requests are generally used to retrieve information.
#
# Go to /docs and you will see:
#
# GET /hello
#
# Click:
#
# Try it out
#     ↓
# Execute
#
# The response will appear in the response box.

@app.get("/hello")
def hello():

    return {
        "message": "Hello from FastAPI!"
    }


#-----------------------------#
#       PATH PARAMETERS       #
#-----------------------------#

# We can put variables directly into the URL.
#
# The {name} part is called a PATH PARAMETER.
#
# FastAPI will take whatever is placed where {name} is
# and pass it into our function.
#
# For example:
#
# /hello/Alex
#
# FastAPI will run:
#
# say_hello(name="Alex")
#
# The /docs interface will automatically give you
# a box where you can enter the name.

@app.get("/hello/{name}")
def say_hello(name: str):

    # ": str" is a type annotation.
    #
    # We are telling FastAPI that "name"
    # should be a string.

    return {
        "message": f"Hello, {name}!"
    }


#-----------------------------#
#       QUERY PARAMETERS      #
#-----------------------------#

# Query parameters are another way to send
# information to an API.
#
# This endpoint expects a parameter called "item".
#
# In /docs, FastAPI will automatically create
# an input box for "item".
#
# You could enter:
#
# Python
#
# Then FastAPI will run:
#
# search(item="Python")

@app.get("/search")
def search(item: str):

    return {
        "searched_for": item,
        "message": f"You searched for {item}!"
    }


#-----------------------------#
#         ADD NUMBERS         #
#-----------------------------#

# We can also use path parameters with numbers.
#
# Here, both "a" and "b" are integers.
#
# In /docs, you can enter:
#
# a = 10
# b = 5
#
# FastAPI will then run:
#
# add_numbers(10, 5)
#
# and return the result.

@app.get("/add/{a}/{b}")
def add_numbers(a: int, b: int):

    return {
        "a": a,
        "b": b,
        "result": a + b
    }


#-----------------------------#
#         POST REQUEST        #
#-----------------------------#

# GET requests are commonly used to retrieve information.
#
# POST requests are commonly used to send or create information.
#
# We create a POST endpoint using:
#
# @app.post()
#
# In /docs, you will see:
#
# POST /users
#
# Click "Try it out" and then "Execute".

@app.post("/users")
def create_user():

    return {
        "message": "User created!"
    }


#-----------------------------#
#        THE BIG IDEA         #
#-----------------------------#

# When you click "Execute" in /docs,
# you are actually sending an HTTP request
# to your FastAPI application.
#
# The process looks something like this:
#
#
#     YOU
#      |
#      | Click "Execute"
#      v
#     /docs
#      |
#      | Sends HTTP request
#      v
#     FASTAPI
#      |
#      | Finds the matching route
#      v
#     PYTHON FUNCTION
#      |
#      | Runs the code
#      v
#     FASTAPI
#      |
#      | Sends the response
#      v
#     /docs
#      |
#      | Displays the JSON response
#      v
#     YOU
#
#
# So the /docs page isn't actually your API.
#
# It is an interface that lets you interact
# with and test your API.


#-----------------------------#
#         EXPERIMENTS         #
#-----------------------------#

# Now try changing the code yourself!
#
# 1. Create a new GET endpoint called "/multiply/{a}/{b}".
#
# 2. Make it multiply the two numbers.
#
# 3. Create a "/favorite/{thing}" endpoint that returns
#    a message about your favorite thing.
#
# 4. Try changing "str" to "int" and see how the
#    /docs interface changes.
#
# 5. Try entering the wrong type of data.
#    For example, enter "hello" when the API expects
#    an integer.
#
# 6. Go to /docs and test all your endpoints.
#
#
# The goal is to understand that:
#
#     @app.get(...)
#
# connects a URL to a Python function.
#
# The function receives information from the request,
# does something with it, and returns a response.
#
# FastAPI then sends that response back to the client.