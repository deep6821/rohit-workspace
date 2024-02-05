"""
Encapsulation:
--------------
Encapsulation in OOP refers to binding the data and the methods to manipulate
that data together in a single unit, that is, class.

Depending upon this unit, objects are created. Encapsulation is usually done to
hide the state and representation of an object from outside. A class can be
thought of as a capsule having methods and properties inside it.

When encapsulating classes, a good convention is to declare all variables of a
class private. This will restrict direct access by the code outside that class.

At this point, a question can be raised that if the methods and variables are
encapsulated in a class, then “how can they be used outside of that class”

Well, the answer to this is simple. One has to implement public methods to let
the outside world communicate with this class. These methods are called getters
and setters. We can also implement other custom methods.

Advantages of Encapsulation:
----------------------------
- Classes make the code easy to change and maintain.
- Properties to be hidden can be specified easily.
- We decide which outside classes or functions can access the class properties.

"""

"""
Consider that we are up for designing an application and are working on modeling the log in part of 
that application. We know that a user needs a username and a password to log into the application.

An elementary User class will be modeled as:
1. Having a property userName
2. Having a property password
3. A method named login() to grant access

Whenever a new user comes, a new object can be created by passing the userName and password to the 
constructor of this class.

In the below coding example, we can observe that anyone can access, change, or print the password and 
user_name fields directly from the main code. This is dangerous in the case of this User class because 
there is no encapsulation of the credentials of a user, which means anyone can access their account by 
manipulating the stored data. So, the above code did not follow good coding practices.
"""


# A Bad Example
class User:
    def __init__(self, user_name=None, password=None):
        self.user_name = user_name
        self.password = password

    def login(self, user_name, password):
        if ((self.user_name.lower() == user_name.lower()) and (
                self.password == password)):
            print("Access Granted!")
        else:
            print("Invalid Credentials!")


obj = User("TT", "12345")
obj.login("TT", "12345")
obj.login("TT", "6789")
obj.password = "6789"
obj.login("TT", "6789")


print("\n--------------------------------------------------------------------")
# A Good Example
class User:
    def __init__(self, user_name=None, password=None):
        self.user_name = user_name
        self.__password = password

    def login(self, user_name, password):
        if ((self.user_name.lower() == user_name.lower()) and (self.__password == password)):
            print(
                "Access Granted against username:",
                self.user_name.lower(),
                "and password:",
                self.__password)
        else:
            print("Invalid Credentials!")


# created a new User object and stored the password and username
obj = User("TT", "12345")
obj.login("TT", "12345")  # Grants access because credentials are valid
# does not grant access since the credentails are invalid
obj.login("TT", "6789")
obj.__password  # compilation error will occur due to this line



class User:
    def __init__(self, user_name=None, password=None):
        self.__username = user_name
        self.__password = password

    def login(self, user_name, password):
        if ((self.__username.lower() == user_name.lower()) and (
                self.__password == password)):
            print(
                "Access Granted against username:",
                self.__username.lower(),
                "and password:",
                self.__password)
        else:
            print("Invalid Credentials!")


# created a new User object and stored the password and username
obj = User("Steve", "12345")
obj.login("steve", "12345")  # Grants access because credentials are valid
# does not grant access since the credentails are invalid
obj.login("steve", "6789")
# obj.__password  # compilation error will occur due to this line
