"""
- Singleton pattern as the name suggests is used to create one and only instance of a class and a global point of access
to it. Ex: Caches, Database connectivity, registries, thread pools etc.

Database connectivity. When each object creates a unique Database Connection to the Database, it will highly affect
the cost and expenses of the project. So, it is always better to make a single connection rather than making extra
irrelevant connections.

                        OR

It is useful in cases were multiple instances will result in an inconsistent state or conflicting requests, such as
multiple Loggers trying to modify the same log file, or multiple database connectors trying to modify the same database.

- By providing us with a single global object, the Singleton pattern allows us to control concurrent access to shared
resources.

- Actually, anytime that we are importing a module in python we are using the Singleton pattern. This is because by
default, when we import a module, Python checks whether the requested module has been already imported. If it does, it
returns that object. If it does not, it imports it and initializes it.

Implementing a Singleton:
-------------------------

- In ‘traditional’ Object-Oriented languages such as Java, the Singleton can be simply implemented by declaring the
constructor as private and defining a static method that calls the private constructor the first time, and returning
the same object from then on.

- Since the option of private constructors in Python does not exist, we will implement it in a different way. As you can
see in the example below, we override the __new__ method with some logic to check whether the object already exists.

Advantages of using Singleton Method:
-------------------------------------
1. Initializations: Object created by Singleton method is initialized only when it is requested for the first time.
2. Access to the object: We got the global access to the instance of the object.
3. Count of instances: In singleton method classes can’t have more than one instance

Disadvantages of using Singleton Method:
---------------------------------------
1. Multithread Environment: Its not easy to use the singleton method in multithread environment, because we have to take
care that multithread wouldn’t create singleton object several times.
2. Single responsibility Principle: As the Singleton method is solving two problems at a single time, it doesn't follow
the single responsibility principle.
3. Unit testing process: As they introduce the global state to the application, it makes the unit testing very hard.

Applicability:
--------------
1. Controlling over global variables: In the projects where we specifically need the strong control over the global
variables, it is highy recommended to use Singleton Method
2. Daily Developers use: Singleton patterns are generally used in providing the logging, caching, thread pools and
configuration settings and oftenly used in conjuction with Factory design pattern.

"""

if 0:
    class Singleton(object):
        def __new__(self):
            if not hasattr(self, 'instance'):
                # Normally the super() method normally gives us access to the parent class, however here because a
                # parent does not exist, we gain access to the current class.
                self.instance = super().__new__(self)
            return self.instance


    obj = Singleton()
    print("Object created: ", obj)
    obj1 = Singleton()
    print("Object created: ", obj1)

if 0:
    """
    Lazy Instantiation of the Singleton Pattern:
    --------------------------------------------
    
    At times that resources are limited or when objects are too demanding in terms of computing resources we may 
    prefer to only create an object when it is really needed. In the example below, the constructor __init__ does not 
    create any new object. Object creation only happens when we explicitly call the getInstance() method
    """


    class Singleton(object):
        __instance = None

        def __init__(self):
            if not Singleton.__instance:
                print("__init__ method called but nothing is created")
            else:
                print("instance already created:", self.get_instance())

        @classmethod
        def get_instance(cls):
            if cls.__instance is None:
                cls.__instance = Singleton()
                return cls.__instance


    obj1 = Singleton()
    obj2 = Singleton()

    # This returns None although the object is initialized
    print(obj1._Singleton__instance)
    print(obj2._Singleton__instance)

    obj1.get_instance()
    obj2.get_instance()

    # Which is now accessible
    print(obj1._Singleton__instance)
    print(obj2._Singleton__instance)

if 0:
    """
    The Monostate Singleton Pattern:
    --------------------------------
    
    - Some programmers consider more important the state and behavior of an object rather than its identity. By this, it 
    is meant that we shouldn't care so much that a single object exists but rather that objects should have a shared 
    state even if we allow for the creation of multiple instances of the class.
    
    - To achieve this shared state, we use the special Python variable __dict__. This variable exists for all 
    user-defined classes and functions and it contains all attributes of the object under question.
    
    - By assigning the __dict__ property in the __init__ method to be equal to an already-created class-property 
    dictionary, we force all instantiations of objects to share the same __dict__ and thus also share attributes 
    (since all attributes are stored in this __dict__ property)
    """


    def func():
        pass


    # User-defined functions have a __dict__ property:
    print("__dict__ of func:", func.__dict__)
    func.temp = 1
    print("__dict__ of func after assignment:", func.__dict__)


    class A:
        def __init__(self, prop):
            self.prop = prop

        def test_func(self):
            print("test function")


    # Class definitions have a __dict__ property:
    print("__dict__ of A:", A.__dict__)

    # Class instantiations have a __dict__ property:
    a = A(123)
    print("__dict__ of a:", a.__dict__)

    print("-------------------------------------- \n")


    class MonostateSingleton:
        __shared_state = {'apikey': 'xxxxxxxxxxxxxxxxxxx'}

        def __init__(self):
            # Because dictionary assignments are by reference, we force
            # self.EOFError__dict__ to be common to all future instantiations
            self.__dict__ = self.__shared_state
            self.x = 1


    obj1 = MonostateSingleton()
    obj2 = MonostateSingleton()

    # Notice that the two objects reside at different addresses, thus
    # they are different objects:
    print("property x: {} of obj at: {}".format(obj1.x, obj1))
    print("property x: {} of obj1 at: {}".format(obj2.x, obj2))

    # Notice that the 'x' property is part of the __dict__
    print(obj1.__dict__, obj2.__dict__)

    # We change the x propert only of obj
    obj1.x = "Rohit"

    # However, because the two objects share the same __dict__ and this is  where class attributes are stored, the
    # change is also visible in obj2 We have thus achieved a SHARED STATE:
    print("property x: {} of obj at: {}".format(obj1.x, obj1))
    print("property x: {} of obj1 at: {}".format(obj2.x, obj2))
    print(obj1.__dict__, obj2.__dict__)

if 0:
    """
    Type is a metaclass of which all classes, even the built-in ones, are instances.
    --------------------------------------------------------------------------------

    => Until now, we have been using type(...) with a single argument which returns the type of the passed object. 
       However, it can also be called with three arguments: type(<name>, <bases>, <dict>) where:

    1. <name> specifies the class name. This becomes the __name__ attribute of the returned class.
    2. <bases> specifies a tuple of the base classes from which the new class will inherit from. This becomes the 
    __bases__ attribute of the class.
    3. <dict> specifies a namespace dictionary containing the definitions of the class body. This becomes the 
    __dict__ attribute of the class.
    
    => What happens is that type(<name>, <bases>, <dict>) is a metaclass that can be used to create (dynamic) classes. 
       The order of execution whenever a concrete standard class’ constructor is called, is the following:

    1. The __call__() method of Foo's parent class is called. Because Foo is a standard class (i.e. it does not inherit 
    from any user-defined parent class), its parent class is the type metaclass, so type's __call__() method is invoked.
    2. The __call__() method in turn invokes the __new__() and __init__() method. If these are not defined in Foo, 
    default methods are inherited, again from type.
    
    => The above is only true when instantiating objects of user-defined classes. If we wanted to modify instantiation 
    behavior when creating classes, we would again define a custom method and assign it as the __new__() method for the 
    class of which Foo is an instance. And this is no other than the type metaclass.
    
    => However, as you can see from [3] below, Python does not let us reassign the __new__() method of type and for good 
    reason: This would modify all classes that inherit from type.
    
    => So, the only way to modify instantiation behavior when creating classes, is to write our own, custom metaclass 
    which will derive from type and the modify the __new__() method of that instead. We can use the same logic in the 
    Singleton design pattern as well: We create a new metaclass called MetaSingleton and override its__call__() method.
    The call method is what invokes the __new__() and __init__() method and by modifying its logic we can make these 
    calls dependent on the existence of the _instances class attribute.
    """


    # since classes are also objects, it must have a type as well
    class Foo:
        pass


    x = Foo()

    # x is of type 'Foo'
    print(type(x), x.__class__)

    # the type of all classes (i.e. the definitions) are of type 'type':
    print(type(Foo), Foo.__class__)

    # the type of familiar built-in classes are also 'type'  AND EVEN type IS OF TYPE 'type':
    for t in (int, float, dict, list, tuple, type):
        print(type(t))

    # We can define a class dynamically, using type(<name>, <bases>, <dict>)
    Bar = type('Bar', (Foo,), dict(attr=100))
    y = Bar()

    print(type(y), y.__class__)
    print(Bar.__bases__)


    ### [2] ###
    # NOTE: this is just for demonstration purposes, normally attribute assignment would be done in the __init__ method

    def new_foo(cls):
        x = object.__new__(cls)
        x.attr = 100
        return x


    # We can modify Foo's __new__ method to customize object instantiation
    Foo.__new__ = new_foo

    x2 = Foo()
    print(x2.attr)


    ### [3] ###
    def new_type(cls):
        x = type.__new__(cls)
        x.attr = 100
        return x


    try:
        type.__new__ = new_foo
    except TypeError:
        print(TypeError.__doc__)


    ### [4] ###

    # The first step is to create a metaclass that derives from type:
    class Meta(type):
        # We then modify the __new__() method of this custom metaclass
        # This wasn't possible to do in 'type' directly
        def __new__(cls, name, bases, dct):
            x = super().__new__(cls, name, bases, dct)
            x.attr = 100
            return x


    # We define the new Class Foo but change its metaclass to 'Meta'
    # using the metaclass keyword in the class definition:
    class Foo(metaclass=Meta):
        pass


    print(Foo.attr)


    ### [5] ###
    class MetaSingleton(type):
        _instances = {}

        def __call__(cls, *args, **kwargs):
            if cls not in cls._instances:
                # now the type's __call__() is only executed if cls is not in cls._instancesThis way we prevent new
                # objects from being created if one exists when the constructor of classes deriving from MetaSingleton
                # are created
                cls._instances[cls] = super().__call__(*args, **kwargs)

            return cls._instances[cls]


    class Logger(metaclass=MetaSingleton):
        pass


    logger1 = Logger()
    logger2 = Logger()

    # logger1 and logger2 refer to the same object
    print(logger1, logger2)

if 1:
    # Using Decorator
    def singleton(MyClass):
        instances = {}

        def get_instance(*args, **kwargs):
            if MyClass not in instances:
                instances[MyClass] = MyClass(*args, **kwargs)
            return instances[MyClass]

        return get_instance

    @singleton
    class Test(object):
        pass

    obj = Test()
    print(obj)
    obj1 = Test()
    print(obj1)

