#-----------------------------#
#           PROPERTY          #
#-----------------------------#

#i know i covered this earlier but this is were i understood this correctly:
#property is a decorator used in encapsulation(not directly iterating the attributes outside of classes). It aids in stopping us from changing an attribute outside of a class without reason

#the most common example is here:

#In a regular account it is impossible for your balance to be negative.
#the withdraw method doesn't allow it.

#but you can literally set Account.balance = -999.
#to preven that we can use property or add _ before any attributes that can't change outside of classes as a reminder
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        self.show_account()

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            self.show_account()

    def show_account(self):
        print(f"{self.owner}'s Balance:{self.balance}")

Jims_account = Account("Jim", 100)

#hacker's doing:
Jims_account.balance = -999
Jims_account.show_account()

class SaferAccountV1:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount
        self.show_account()

    def withdraw(self, amount):
        if self._balance > amount:
            self._balance -= amount
            self.show_account()

#but as you can see above just adding a _ before an attribute will not stop hackers(farfetched) from setting your bank accoun to -999

#but that is were @property comes in
class SaferAccountV2:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount
        self.show_account()

    def withdraw(self, amount):
        if self._balance > amount:
            self._balance -= amount
            self.show_account()

    def show_account(self):
        print(f"Balance: {self._balance}")

    @property
    def balance(self):
        return self._balance
    
Jhons_account = SaferAccountV2("Jhon", 50)
#when hackers try this: 
#Jhons_account.balance = -19
#they will get an error
print(Jhons_account.balance)
#note:
#account._balance = -19(it is intended, not enforced)   →  Python allows it
#account.balance = -19    →  Property blocks it


#okay, okay but for now. now for real.
#here is a way to do that:

class SaferAccountV3:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    

    def deposit(self, amount):
        self._balance += amount
        self.show_account()

    def withdraw(self, amount):
        if self._balance > amount:
            self._balance -= amount
            self.show_account()

    def show_account(self):
        print(f"Balance: {self._balance}")

    @property
    def balance(self):
        return self._balance

    #Note: the setter is only designed to take one arguement.
    @balance.setter
    def balance(self, value):
        if self._balance<0:
            print("balance can't be negative")
        else:
            self._balance -= value

carlos = SaferAccountV3("carlos", 100)
#carlos.balance = -1
#the setter is only triggered when it sees something like this:
carlos._balance = 110

#                         OOP
#                          │
#              ┌───────────┴───────────┐
#              │                       │
#          Classes                  Objects
#                                      │
#                              ┌───────┴────────┐
#                              │                │
#                       Instance attrs     Class attrs
#                              │                │
#                       self.name          school
#                       self.grade         population
#                       self.balance       species
#                              │                │
#                       Belong to ONE      Belong to
#                         object            the CLASS

#note:
# class attrs have a univeral shared value among objects
# instance attrs have unique values among eachother                                  