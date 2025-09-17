from abc import ABC,abstractmethod

# ---------- Strategy Interface ----------
class Strategy:

    @abstractmethod
    def execute(self,a,b):
        pass

# ---------- Concrete Stratgy ----------
class AddStrategy(Strategy):

    def execute(self,a, b):
        return a+b

class SubstractStrategy(Strategy):

    def execute(self,a, b):
        return a-b

class MultiplyStrategy(Strategy):

    def execute(self,a, b):
        return a*b

# ---------- Context ----------
class Context:

    def __init__(self) -> None:
        self._strategy:Strategy= None
    
    def setStrategy(self,str:Strategy):
        self._strategy= str
    
    def executeStrategy(self,a,b):
        return self._strategy.execute(a,b)


if __name__== "__main__":

    context= Context()
    addStr= AddStrategy()
    context.setStrategy(addStr)
    ans= context.executeStrategy(10,20)
    print(f"Ans using Add strategy {ans}")

    mulStr= MultiplyStrategy()
    context.setStrategy(mulStr)
    ans= context.executeStrategy(10,20)
    print(f"Ans using Multiply strategy {ans}")