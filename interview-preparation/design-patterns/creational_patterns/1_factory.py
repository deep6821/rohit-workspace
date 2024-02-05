"""
1. Simple factory: Although not really considered a pattern, it provides a simple way to decouple our system
from concrete classes.
2. Factory method: It relies on inheritance to delegate object creation to the subclasses, which decide what
objects get created by implementing the factory method.
"""

if 1:
    """
    The Simple Factory Pattern
    --------------------------

    The Pizza shop needs to produce different kinds of pizzas. A simple way to do this would be to have an 
    orderPizza() method that takes a pizzaType argument and based on that the right type of pizza is prepared.

    However, changing food trends means that this method will need to change often: In the near future we may 
    want to add some more types of pizzas and remove a few unpopular ones. The current design violates the 
    single responsibility principle since our current method is open for modification.

    A simple solution, is to encompass the pizza creation into a new object as you can see in [2] below. We 
    call such an object a factory. This new object encompasses everything that changes (in this case the pizza
    creation process, depending on the type of pizza). The PizzaStore's orderPizza() method only needs to be 
    aware of the factory’s  createPizza() method and the rest is handled by the pizza factory.

    """

    from abc import abstractmethod, ABC


    ###################### [1] ######################
    class Pizza(ABC):

        @abstractmethod
        def prepare(self):
            pass

        def bake(self):
            print("baking pizza for 12min in 400 degrees..")

        def cut(self):
            print("cutting pizza in pieces")

        def box(self):
            print("putting pizza in box")


    class CheesePizza(Pizza):
        def prepare(self):
            print("preparing a cheese pizza..")


    class GreekPizza(Pizza):
        def prepare(self):
            print("preparing a greek pizza..")


    def orderPizza(pizzaType: str):
        # orderPizza needs to be aware of the pizza creation task. this is violating the single responsibility principle
        # since our code is open for modification
        if pizzaType == 'Greek':
            pizza = GreekPizza()
        elif pizzaType == 'Cheese':
            pizza = CheesePizza()
        else:
            print("No matching pizza found...")

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()


    print("##### [1] ########")
    orderPizza('Greek')
    print("##################\n")


    ###################### [2] ######################

    # We can instead create a Simple Factory that will exclusively deal with the pizza creation process.
    class SimplePizzaFactory:
        def createPizza(self, pizzaType: str) -> Pizza:
            pizza: Pizza = None

            if pizzaType == 'Greek':
                pizza = GreekPizza()
            elif pizzaType == 'Cheese':
                pizza = CheesePizza()
            else:
                print("No matching pizza found...")

            return pizza


    class PizzaStore:
        factory: SimplePizzaFactory

        def __init__(self, factory: SimplePizzaFactory):
            self.factory = factory

        def orderPizza(self, pizzaType: str):
            # orderPizza only needs to be aware of preparing the pizza.
            # we have encompassed everything
            pizza: Pizza
            pizza = self.factory.createPizza(pizzaType)

            pizza.prepare()
            pizza.bake()
            pizza.cut()
            pizza.box()


    #################################################
    store = PizzaStore(SimplePizzaFactory())

    print("##### [2] ########")
    store.orderPizza('Greek')
    print("##################\n")

if 1:
    """
    The Factory Method Pattern:
    ---------------------------

    Our current design still has some issues though. For example what happens if we want to create 
    New York/Chicago/California-styled pizzas? One way to solve this is the following:

    1. First we bring back the createPizza() method into the PizzaStore however, this time it is declared as an abstract 
    method.
    2. This makes the PizzaStore an abstract class from which we can derive NY pizza stores, Chicago pizza stores and 
    so on. These stores, which will be subclasses of PizzaStore, will need to override the now abstract createPizza() 
    method. In essence, what this does is let the subclass decide via its definition of createPizza(). This is because 
    the orderPizza() is defined in the abstract PizzaStore class and in its body, the abstract createPizza() method is 
    called. This means that orderPizza() itself has no idea which pizza is going to get created until we actually 
    create a concrete subclass of PizzaStore.

    What we achieved is to encompass all responsibility for instantiating Pizzas into a method that acts as a factory. 
    This factory method needs to be abstract so that it is left up to the subclasses to determine the specific object 
    creation.
    """

    from abc import ABC, abstractmethod


    class Pizza(ABC):

        @abstractmethod
        def prepare(self):
            pass

        def bake(self):
            print("baking pizza for 12min in 400 degrees..")

        def cut(self):
            print("cutting pizza in pieces")

        def box(self):
            print("putting pizza in box")


    class NYStyleCheesePizza(Pizza):
        def prepare(self):
            print("preparing a New York style cheese pizza..")


    class ChicagoStyleCheesePizza(Pizza):
        def prepare(self):
            print("preparing a Chicago style cheese pizza..")


    class NYStyleGreekPizza(Pizza):
        def prepare(self):
            print("preparing a New York style greek pizza..")


    class ChicagoStyleGreekPizza(Pizza):
        def prepare(self):
            print("preparing a Chicago style greek pizza..")


    # This time, PizzaStore is abstract
    class PizzaStore(ABC):

        # We brought createPizza back into the PizzaStore (instead of the SimpleFactory)
        # However, it is declared as abstract. This time, instead of having
        # a factory class, we have a factory method:
        @abstractmethod
        def _createPizza(self, pizzaType: str) -> Pizza:
            pass

        def orderPizza(self, pizzaType):
            pizza: Pizza

            pizza = self._createPizza(pizzaType)

            pizza.prepare()
            pizza.bake()
            pizza.cut()
            pizza.box()


    class NYPizzaStore(PizzaStore):

        def _createPizza(self, pizzaType: str) -> Pizza:
            pizza: Pizza = None

            if pizzaType == 'Greek':
                pizza = NYStyleGreekPizza()
            elif pizzaType == 'Cheese':
                pizza = NYStyleCheesePizza()
            else:
                print("No matching pizza found in the NY pizza store...")

            return pizza


    class ChicagoPizzaStore(PizzaStore):

        def _createPizza(self, pizzaType: str) -> Pizza:
            pizza: Pizza = None

            if pizzaType == 'Greek':
                pizza = ChicagoStyleGreekPizza()
            elif pizzaType == 'Cheese':
                pizza = ChicagoStyleCheesePizza()
            else:
                print("No matching pizza found in the Chicago pizza store...")

            return pizza


    nyPizzaStore = NYPizzaStore()
    chPizzaStore = ChicagoPizzaStore()

    nyPizzaStore.orderPizza('Greek')
    print("\n")
    chPizzaStore.orderPizza('Cheese')