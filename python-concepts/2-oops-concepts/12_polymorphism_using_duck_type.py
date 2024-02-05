"""
What is Duck Typing?
- We say that if an object quacks like a duck, swims like a duck, eats like a
  duck or in short, acts like a duck, that object is a duck.

- Duck typing extends the concept of dynamic typing in Python.

Dynamic typing:  means we can change the type of an object later in the code.
"""
x = 5  # type of x is an integer
print(type(x))

x = "TT"  # type x is now string
print(type(x))

print("\n ------------------------------------------------------------------")


class Dog:
    def Speak(self):
        print("Woof woof")


class Cat:
    def Speak(self):
        print("Meow meow")


class AnimalSound:
    def Sound(self, animal):
        animal.Speak()


sound = AnimalSound()
dog = Dog()
cat = Cat()

sound.Sound(dog)
sound.Sound(cat)


"""
In the above example, animal object does not matter in the definition of the 
Sound method as long as it has the associated behavior, speak(), defined in 
the object’s class definition. In layman terms, since both the animals, dog 
and cats, can speak like animals, they both are animals. 

This is how we have achieved polymorphism without inheritance.
"""