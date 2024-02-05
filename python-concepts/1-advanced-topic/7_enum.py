"""
Enumerations in Python are implemented by using the module named “enum“.
Enumerations are created using classes. Enums have names and values associated with them.

Properties of enum:
1. Enums can be displayed as string or repr.
2. Enums can be checked for their types using type().
3. “name” keyword is used to display the name of the enum member.


"""
import enum


class Animal(enum.Enum):
    dog = 1
    cat = 2
    lion = 3


print("The string representation of enum member is : ", end="")
print(Animal.dog, type(Animal.dog))

# printing enum member as repr
print("The repr representation of enum member is : ", end="")
print(repr(Animal.dog))

# printing the type of enum member using type()
print("The type of enum member is : ", end="")
print(type(Animal.dog))

# printing name of enum member using "name" keyword
print("The name of enum member is : ", end="")
print(Animal.dog.name)

# 4. Enumerations are iterable. They can be iterated using loops
print("All the enum values are : ")
for i in Animal:
    print(i)

# 5. Enumerations support hashing. Enums can be used in dictionaries or sets.
di = {}
di[Animal.dog] = 'bark'
di[Animal.lion] = 'roar'
if di == {Animal.dog: 'bark', Animal.lion: 'roar'}:
    print("Enum is hashed")
else:
    print("Enum is not hashed")

print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
for i in Animal:
    print(i.value)
print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# Comparison : Enumerations supports two types of comparisons
# 1. Identity :- These are checked using keywords “is” and “is not“.
# 2. Equality :- Equality comparisons of “==” and “!=” types are also supported

# Accessing enum member using value
print("The enum member associated with value 2 is : ", end="")
print(Animal(2))

# Accessing enum member using name
print("The enum member associated with name lion is : ", end="")
print(Animal['lion'])

# Assigning enum member
mem = Animal.dog

# Displaying value
print("The value associated with dog is : ", end="")
print(mem.value)

# Displaying name
print("The name associated with dog is : ", end="")
print(mem.name)

# Comparison using "is"
if Animal.dog is Animal.cat:
    print("Dog and cat are same animals")
else:
    print("Dog and cat are different animals")

# Comparison using "!="
if Animal.lion != Animal.cat:
    print("Lions and cat are different")
else:
    print("Lions and cat are same")
