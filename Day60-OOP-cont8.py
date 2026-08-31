#-----------------------------#
#       SELF RECAP+NOTES      #
#-----------------------------#
#the self method is kind of hard to understand but here is what i know about it now:

#self is a reference to whatever object calling a method inside a class(inheritance doesn't matter):
#self can be anything it is just purely convention:

class employee:
    #in this constructor i decided to call it inst, short for instance
    def __init__(inst, fname, lname, age):
        inst.fname = fname
        inst.lname = lname
        inst.age = age
        inst.email = f"{inst.fname}.{inst.lname}@gmail.com"

    def introduce(inst, listeners_name):
        return f"Hi, {listeners_name}! im {inst.fname} {inst.lname} and im {inst.age} years old. You can contact me through {inst.email}"


#as you can see in the above class i am going to create an instance of employee(me)

intern_1 = employee("Mahathish", "P", 13)

#but notice that we never give any value to the inst(self) parameter? it is because intern_1 under the hood is a parameter
print(intern_1.introduce("Boss"))

#it may not sound obvious but secretly in the background this is what python is doing:
#as you can see, we are indeed passing two arguments
print(employee.introduce(intern_1, "Boss"))

#so methodically speaking, yes. self(inst) is refering to the object that is calling/using the method

#-----------------------------#
#        CLASS VARIABLES      #
#-----------------------------#

#class variables are like attributes to objects but all objects share the same value
#like in the above example intern_1's fname and some new objects fname attribute don't have to be the same
#but a variable called company might be.

class employee:
    #this is how you create these types of class variables:
    raise_amount = 1.04

    #decided to call it self to follow convention:
    def __init__(self, fname, lname, age, pay):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.email = f"{self.fname}.{self.lname}@gmail.com"
        self.pay = pay

    def give_raise(self):
        #since the object isn't going to have a raise_amount var in it's list of attribute values we are telling it where to get it from
        #you can also use the self parameter instead of the employee because we can let python search for it.
        self.pay = self.pay*employee.raise_amount

#here goes nothing:

emp_1 = employee("Gary", "Mitchell", 49, 70000)

#python checks the object. then searches for it in other places
print(emp_1.raise_amount)
print("-"*25)

#but if it can't find it, it will make one and give it a value:
#notice how these are separate values?
emp_1.raise_amount = 1.06
print(emp_1.raise_amount)
print(employee.raise_amount)

#okay here is when to use what:
#when you think we should be able to change a value for a specific scenario but keep it something else in other cases, use self
#when the value has to be same across all objects, use employee or whatever class name you have

