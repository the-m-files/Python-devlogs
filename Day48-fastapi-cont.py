#-----------------------------#
#          FASTAPI            #
#-----------------------------#

#FastAPI is a Python framework used to build web APIs.
#Think of it as the "backend" of a website.
#It receives requests from a browser and sends responses back.

from fastapi import FastAPI

#this creates our FastAPI application
app = FastAPI()


#the @app.get("/") decorator tells FastAPI:
#"when someone visits the home page,
#run the function below."

@app.get("/")
def home():
    return {"message": "Hello, World!"}


#the "/" is called a route
#it represents the homepage of our API

#the function returns a Python dictionary
#FastAPI automatically converts it into JSON

#Python:
#{"message": "Hello, World!"}

#becomes JSON:
#{
#    "message": "Hello, World!"
#}


#we can create multiple routes

@app.get("/about")
def about():
    return {"about": "This is my first API."}


@app.get("/favoritecolor")
def favorite_color():
    return {"color": "Blue"}


#to run our app:
#
#fastapi dev filename.py
#
#or
#
#uvicorn filename:app --reload
#
#then open:
#http://127.0.0.1:8000


#you can also visit:
#http://127.0.0.1:8000/docs
#
#FastAPI automatically creates documentation
#for every route you make.


#the gist:

#app = FastAPI()

#@app.get("/")

#def home():
#    return {"message": "Hello"}

#FastAPI waits for a request.
#If someone visits "/",
#it runs home().
#The returned dictionary is converted into JSON
#and sent back to the browser.