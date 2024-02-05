"""
- A generator function is defined like a normal function, but instead of returning a result they
instead yield a value and when a yield a value it keeps that state until the generator is run again
and yields that next value.

- So generators are iterators as well but the dunder __iter__ and __next__ methods are created
automatically, so we don't have to create them like we did in our class.

"""


def generator(start, end):
    current = start
    while current < end:
        yield current
        current += 1


def square(nums):
    result = []
    for i in nums:
        yield i * i  # result.append(i*i)


nums = generator(1, 10)
print(next(nums))
print("\n++++++++++++++++++++")
for num in square([1, 2, 3, 4]):
    print(num)


"""
- The yield statement suspends function’s execution and sends a value back to the caller, but retains enough state
to enable function to resume where it is left off. When resumed, the function continues execution immediately
after the last yield run. This allows its code to produce a series of values over time, rather than computing
them at once and sending them back like a list.

- Return sends a specified value back to its caller whereas Yield can produce a sequence of values. We should use
yield when we want to iterate over a sequence, but don’t want to store the entire sequence in memory.

- Yield are used in Python generators. A generator function is defined like a normal function, but whenever it
needs to generate a value, it does so with the yield keyword rather than return. If the body of a def contains
yield, the function automatically becomes a generator function.

"""


def simple_generator_fun():
    yield 1
    yield 2
    yield 3


# A Python program to generate squares from 1 to 100 using yield and therefore generator
def next_square():
    i = 1
    # An Infinite loop to generate squares
    while True:
        yield i * i
        i += 1  # Next execution resumes from this point


for value in simple_generator_fun():
    print(value)

for num in next_square():
    print("=========")
    if num > 100:
        break
    print(num)