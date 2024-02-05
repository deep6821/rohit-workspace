"""
First Class Function:
- A programming language is said to have first class functions, if it is treats functions as
first class citizens.

First Class Citizens:
- A first class citizens(some times called first class object) in a programming language is an entity
which supports all the operations generally available to other entities.
- These operations typically includes being
1. passed as argument
2. return from a function and
3. assigned to a variable
"""


# Assigned to a variable:
def square(x):
    return x * x


print(square)
f = square(5)
print(f)

print("\n=========================")
f = square
print(f(5))

"""
Passed function as a argument and returned function as the result of the other function: If the function 
accepts other function as a argument or returned function as their result that's we called Higher Order Function.
"""
print("\n+++++++++++++++++++++++++++++++++")


# Returned a function from another function:
def logger(msg):
    def log_message():
        print("Log: ", msg)

    return log_message


log_hi = logger("Hi")
print("????? ---->", log_hi)
log_hi()

"""
From above step to when we executed the log_hi() function at this step, that is remember our initial
message that we passed in to the initial logger function, now this is what we call closer.
"""
