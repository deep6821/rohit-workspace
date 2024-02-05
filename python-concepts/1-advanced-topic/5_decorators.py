"""
- A decorators is a just a function, that takes another function as an argument, add some kind of functionality
and then returns another function, all of this without altering the source code of the original function that
passed in.
"""
import math
import time


# decorator to calculate duration taken by any function.
def calculate_time(func):
    print("func --->>>>>", func)

    # added arguments inside the inner1, if function takes any arguments,
    # can be added like this.
    def inner1(*args, **kwargs):
        # storing time before function execution
        begin = time.time()
        result = func(*args, **kwargs)
        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)
        return result

    return inner1


# this can be added to any function present, in this case to calculate a factorial
@calculate_time
def factorial(num):
    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    time.sleep(2)
    result = math.factorial(num)
    return result


# calling the function.
print(factorial(10))
