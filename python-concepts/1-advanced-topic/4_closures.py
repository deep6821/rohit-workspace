"""
A closer is an inner function that remembers and has access to a variables in the local scope and
which it was created even after the outer function has finished executing.
"""


def outer_function():
    messsage = "Hello"

    def inner_function():
        print(messsage)

    return inner_function


outer_func = outer_function()
print(outer_func())  # ()-->> means executing the function
