"""
Iterables:
----------
- On a higher level, it simply means that, it is something that can be looped over.
- Python list is iterables, but it is not an iterators

Ex: nums = [1, 2, 3]
for num in nums:   --> It is using dunder method ==> __iter__
    print(num)

print(nums) --> If something is iterables, it needs to have special dunder method __iter__

Iterator:
---------

- An iterator is an object with a state so that it remember where is during iteration and iterator also
know how to get the next value

- To get the next value it uses special dunder __next__ method.

Ex:
nums = [1, 2, 3]
next(nums) ---> TypeError: 'list' object is not an iterator

i_nums = iter(nums)
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
print(next(i_nums)) --> StopIteration: while True:
                                            try:
                                                item = next(i_nums)
                                                print(item)
                                            except stopIteration:
                                                break

"""


class CustomIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        # It will return object
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        current = self.start
        self.start += 1
        return current


if __name__ == "__main__":
    nums = CustomIterator(1, 10)
    # for num in nums:
    #     print(num)

    print(next(nums))
