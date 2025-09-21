from abc import ABC,abstractmethod

# ---------- Component Interface ----------
class Coffee(ABC):

    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass 

# ---------- Concrete Componenet ----------
class SimpleCoffee(Coffee):

    def cost(self):
        return 100

    def description(self):
        return "Simple Coffee"

# ---------- Base Decorator ----------
class CoffeeDecorator(Coffee):

    def __init__(self,coffee:Coffee) -> None:
        self._coffee= coffee

# ---------- Concrete Decorators ----------
class MilkDecorator(CoffeeDecorator):

    def cost(self):
        return self._coffee.cost() + 10

    def description(self):
        return self._coffee.description() + f", milk"

class SugarDecorator(CoffeeDecorator):

    def cost(self):
        return self._coffee.cost() + 20

    def description(self):
        return self._coffee.description() + f", sugar"

class WhippedCreamDecorator(CoffeeDecorator):

    def cost(self):
        return self._coffee.cost() + 20

    def description(self):
        return self._coffee.description() + f", whipped cream"

if __name__=="__main__":

    coffee= SimpleCoffee()
    print(coffee.description(), "=> $", coffee.cost())

    milkCoffee= MilkDecorator(SimpleCoffee())
    print(milkCoffee.description(), "=> $", milkCoffee.cost())

    sugarCoffee= SugarDecorator(SimpleCoffee())
    print(sugarCoffee.description(), "=> $", sugarCoffee.cost())

    milkSugarCoffee= MilkDecorator(SugarDecorator(SimpleCoffee()))
    print(milkSugarCoffee.description(), "=> $", milkSugarCoffee.cost())
