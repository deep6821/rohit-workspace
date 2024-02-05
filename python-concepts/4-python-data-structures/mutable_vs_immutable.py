"""
Mutable Objects: In simple words, an mutable object can be changed after it
                 is created.
    Ex: list, dict, set. Custom classes are generally mutable.

Immutable Objects: In simple words, an immutable object can’t be changed after
                  it is created.
    Ex: int, float, bool, string, unicode, tuple




List:
-----
- Lists are just like dynamic sized arrays, declared in other languages.
- Lists need not be homogeneous(A single list may contain DataTypes like Integers, Strings, as well
  as Objects)
- Lists are mutable, and hence, they can be altered even after their creation.
- List in Python are ordered and have a definite count. The elements in a list are indexed according
  to a definite sequence and the indexing of a list is done with 0 being the first index.

Note- Lists are a useful tool for preserving a sequence of data and further iterating over it.

** Each element in the list has its definite place in the list, which allows duplicating of elements
in the list, with each element having its own distinct place and credibility.

Creating a List:
----------------
- Lists in Python can be created by just placing the sequence inside the square brackets[].
Ex: list = []

List Methods:
-------------
1. Append(): Adds its argument as a single element to the end of a list. The length of the list
increases by one. Time Complexity: constant time complexity i.e.,O(1).

Ex: my_list = ['TT']
my_list.append('pandey') --> ['TT', 'pandey']

NOTE: A list is an object. If you append another list onto a list, the parameter list will be a
single object at the end of the list.

Ex: my_list =  ['TT', 'pandey']
another_list = [1, 2, 3]
my_list.append(another_list) --> ['TT', 'pandey', [1, 2, 3]]

2. extend(): Iterates over its argument and adding each element to the list and extending the list.
The length of the list increases by number of elements in it’s argument. Time Complexity: time
complexity of O(k). Where k is the length of list which need to be added.

Ex: my_list = ['TT', 'pandey']
another_list = [1, 2, 3]
my_list.extend(another_list) --> ['TT', 'pandey', 1, 2, 3]

NOTE: A string is an iterable, so if you extend a list with a string, you’ll append each character
as you iterate over the string.

Ex: my_list = ['TT', 'pandey', 1, 2, 3]
another_list = ["rewa"]
my_list.extend(another_list) --> ['TT', 'pandey', 1, 2, 3, 'r', 'e', 'w', 'a']

3. insert(): This method inserts an element at the position mentioned in its arguments. It takes 2
arguments, position and element to be added at respective position.

Ex: lis = [1, 2, 3, 5, 6]
lis.insert(3, 4)

4. remove() :- This function is used to delete the first occurrence of number mentioned in its
arguments.

Ex: lis.remove(3)

5. pop() :- This method deletes the element at the position mentioned in its arguments. By default
it will return last element.

6. Clear():	Removes all items from the list.

7. Index():	Returns the index of the first matched item.

8. Count(): Returns the count of number of items passed as an argument.

9. sort(): Sort items in a list in ascending order.(It will sort same list)

10. Reverse()	Reverse the order of items in the list.

----------------------------------------------------------------------------------------------------

Dictionary:
----------
- It is an unordered collection of key, values, used to store data values like a map, which
  unlike other Data Types that hold only single value as an element, Dictionary holds key:value pair.
  Key value is provided in the dictionary to make it more optimized.

Note – Keys in a dictionary doesn’t allows Polymorphism.

Creating a Dictionary:
----------------------
- In Python, a Dictionary can be created by placing sequence of elements within curly {} braces,
separated by ‘comma’. Dictionary holds a pair of values, one being the Key and the other
corresponding pair element being its Key:value. Values in a dictionary can be of any datatype and
can be duplicated, whereas keys can’t be repeated and must be immutable.

Note – Dictionary keys are case sensitive, same name but different cases of Key will be treated
distinctly.

Dictionary Methods:
-------------------
1. get(): It is a conventional method to access a value for a key.
2. del():
3. pop():
4. popitem(): It removes the arbitrary key-value pair from the dictionary and returns it as a
   tuple. There is an update for this method from Python version 3.7 onwards that it removes the
   last inserted key-value pair from the dictionary and returns it as a tuple.

   Ex: test_dict = { "TT" : 1, "pandey" : 2, "test" : 3}
   res = test_dict.popitem()
   print(res) --> { "TT" : 1, "pandey" : 2}

   Practical Application: This particular function can be used to formulate the random name for
   playing a game or deciding the random ranklist without using any random function.

   for i in range(0, len(test_dict)):
       print ("Rank " + str(i + 1) + " " + str(test_dict.popitem()))

5. clear(): The clear() method removes all items from the dictionary.
   Ex: dict.clear() --> doesn't take any parameters/return any value

"""


class CreateDictionary:
    def __init__(self):
        self.size = 10
        self.bucket = [None] * self.size

    def hash_function(self, key):
        """
        This function will return index for a given key
        :param key: str: name
        :return: int: index for a given key
        """
        hash_value = 0
        for char in key:
            hash_value += ord(char)  # for calculating ascii value

        return hash_value % self.size

    def set(self, key, value):
        arr = [key, value]
        key_hash_index = self.hash_function(key)
        if self.bucket[key_hash_index] is None:
            self.bucket[key_hash_index] = list([arr])
            return True
        else:
            for pair in self.bucket[key_hash_index]:
                if pair[0] == key:
                    pair[1] = value
                else:
                    pass

            self.bucket[key_hash_index].append(arr)

    def __setitem__(self, key, value):
        return self.set(key, value)

    def get(self, key):
        key_hash_index = self.hash_function(key)
        if self.bucket[key_hash_index] is None:
            return None

        else:
            for pair in self.bucket[key_hash_index]:
                if pair[0] == key:
                    return pair[1]

            return None

    def __getitem__(self, item):
        return self.get(item)

    def delete(self, key):
        key_hash_index = self.hash_function(key)
        if self.bucket[key_hash_index] is None:
            return None
        else:
            for pair in range(0, len(self.bucket[key_hash_index])):
                self.bucket[key_hash_index].pop()
                return True

            return None

    def __str__(self):
        return "{}".format(self.bucket)


if __name__ == "__main__":
    d = CreateDictionary()
    # num = d.hash_function("apple")
    # print("????", num, type(num))

    # d.set("name", "Rohit")
    # print(d)

    # Over ride the set method
    d["name"] = "Rohit"
    print(d)

    # name = d.get("name")
    # print("result :", name)

    # Over ride the get method
    print(d["name"])

    # Delete the keys
    d.delete("name")
    print(d)

"""
Sets:
-----

- In Python, Set is an unordered collection of data type that is iterable, mutable and has no 
  duplicate elements. The order of elements in a set is undefined though it may consist of various 
  elements.

- The major advantage of using a set, as opposed to a list, is that it has a highly optimized method 
  for checking whether a specific element is contained in the set.
  
Creating a Set:
--------------
- Sets can be created by using the built-in set() function with an iterable object or a sequence by 
  placing the sequence inside curly braces, separated by ‘comma’.

Note – A set cannot have mutable elements like a list, set or dictionary, as its elements.

Ex: 
set1 = set() 
set1 = set("RohitKumarRohit") 
set1 --> {'o', 'h', 'u', 'K', 'm', 'a', 'r', 'R', 't', 'i'} --> unique but unordered

Methods:
--------

1. add(): Elements can be added to the Set by using built-in add() function. Only one element at a 
   time can be added to the set by using add() method, loops are used to add multiple elements at a 
   time with the use of add() method.
   
Note – Lists cannot be added to a set as elements because Lists are not hashable whereas Tuples can 
be added because tuples are immutable and hence Hashable.

Ex: set1 = set() 
set1.add(8) 
set1.add(9) 
set1.add((6,7))
print(set1) -->  {8, 9, (6, 7)}

set1.add([8,9]) --> TypeError: unhashable type: 'list'


"""